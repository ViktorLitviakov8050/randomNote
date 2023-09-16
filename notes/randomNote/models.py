from django.db import models
from helpers import camel_snake_case, convert_time_from_usec_to_timezoned_utc

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

    name = models.TextField()

class Attachment(models.Model, JSONSourceable):
    accepted_json_attributes = ['filePath', 'mimeType']
    file_path = models.TextField()
    mime_type = models.TextField()
    note =  models.ForeignKey('Note', on_delete=models.CASCADE, related_name='attachments')

class Note(models.Model, JSONSourceable):
    accepted_json_attributes = ['textContent', 'title', 'isArchived']
    text_content = models.TextField(null=True)
    title = models.TextField(null=True)
    edited_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(null=True)
    is_archived = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label)

    # MANY to MANY
    # note.labels | note has many labels
    # label.notes | label has many notes


    # ONE to MANY
    # note.attachments | note has many attachments
    # attachment.note  | attachment has one(!) note
    
    @classmethod
    def from_dict(cls, dictionary):
        note = super().from_dict(dictionary)
        note.created_time = convert_time_from_usec_to_timezoned_utc(dictionary['createdTimestampUsec'])
        note.edited_time = convert_time_from_usec_to_timezoned_utc(dictionary['userEditedTimestampUsec'])

        note.save()

        if 'attachments' in dictionary:
            for attachment_raw in dictionary['attachments']:
                attachment = Attachment.from_dict(attachment_raw)
                attachment.note = note
                attachment.save()

        if 'labels' in dictionary:
            for label_raw in dictionary['labels']:
                label = Label.from_dict(label_raw)
                label.save()
                note.labels.add(label)
        return note
