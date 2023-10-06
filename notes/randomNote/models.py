from django.db import models
from helpers import camel_snake_case, convert_time_from_usec_to_timezoned_utc, copy_file
from random import choice
from django.conf import settings


class JSONSourceable:
    def __repr__(self):
        return '\n'.join([f"{field}: {getattr(self, field)}" for field in self.__dict__])

    @classmethod
    def from_dict(cls, dictionary):
        obj = cls()
        for key, value in dictionary.items():
            if key in cls.accepted_json_attributes:
                setattr(obj, camel_snake_case(key), value)

        return obj


class Label(models.Model, JSONSourceable):
    accepted_json_attributes = ['name']
    name = models.TextField(unique=True)


class Attachment(models.Model, JSONSourceable):
    accepted_json_attributes = ['filePath', 'mimeType']
    file_path = models.TextField()
    mime_type = models.TextField()
    note = models.ForeignKey(
        'Note', on_delete=models.CASCADE, related_name='attachments')


class ListItem(models.Model, JSONSourceable):
    accepted_json_attributes = ['text', 'isChecked']
    text = models.TextField()
    is_checked = models.BooleanField(default=False)
    note = models.ForeignKey(
        'Note', on_delete=models.CASCADE, related_name='list_items')


class Note(models.Model, JSONSourceable):
    accepted_json_attributes = ['textContent', 'title', 'isArchived']
    text_content = models.TextField(null=True, default="")
    title = models.TextField(null=True, default="")
    edited_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(null=True)
    is_archived = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label)

    @classmethod
    def random_note(cls):
        id_array = cls.objects.values_list('id', flat=True)
        random_id = choice(id_array)
        return cls.objects.get(id=random_id)

    @classmethod
    def from_dict(cls, dictionary):
        note = super().from_dict(dictionary)
        note.created_time = convert_time_from_usec_to_timezoned_utc(
            dictionary['createdTimestampUsec'])
        note.edited_time = convert_time_from_usec_to_timezoned_utc(
            dictionary['userEditedTimestampUsec'])

        note.save()

        if 'attachments' in dictionary:
            for attachment_raw in dictionary['attachments']:
                attachment = Attachment.from_dict(attachment_raw)
                attachment.note = note
                attachment.save()

        if 'listContent' in dictionary:
            for list_item_raw in dictionary['listContent']:
                list_item = ListItem.from_dict(list_item_raw)
                list_item.note = note
                list_item.save()

        if 'labels' in dictionary:
            for label_raw in dictionary['labels']:
                try:
                    label = Label.objects.get(name=label_raw["name"])
                except Label.DoesNotExist:
                    label = Label.from_dict(label_raw)
                    label.save()
                note.labels.add(label)
        return note
