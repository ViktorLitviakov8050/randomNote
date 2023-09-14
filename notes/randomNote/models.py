from django.db import models
    
class Label(models.Model):
    name = models.TextField()

class Attachment(models.Model):
    file_path = models.TextField()
    mime_type = models.TextField()
    note =  models.ForeignKey('Note', on_delete=models.CASCADE,related_name='attachments')

class Note(models.Model):
    textContent = models.TextField(null=True)
    title = models.TextField(null=True)
    edited_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(null=True)
    isArchived = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label)
