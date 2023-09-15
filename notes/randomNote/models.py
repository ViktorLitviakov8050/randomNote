from django.db import models
from helpers import camel_snake_case
import datetime

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
        note.created_time = datetime.datetime.utcfromtimestamp(dictionary['createdTimestampUsec']/1000000)
        note.edited_time = datetime.datetime.utcfromtimestamp(dictionary['userEditedTimestampUsec']/1000000)

        if 'attachments' in dictionary:
            for attachment in dictionary['attachments']:
                note.attachments.append(Attachment.from_dict(attachment))

        if 'labels' in dictionary:
            for label in dictionary['labels']:
                note.labels.append(Label.from_dict(label))
        return note
