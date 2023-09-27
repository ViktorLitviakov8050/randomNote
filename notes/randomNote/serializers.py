from rest_framework import serializers
from .models import Note, Attachment, Label

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ["id", "file_path"]

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["id", "name"]        

class NoteSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True)
    labels = LabelSerializer(many=True)
    class Meta:
        model = Note
        fields = "__all__"
