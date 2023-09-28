from rest_framework import views
from .models import Note, Attachment 
from django.http import JsonResponse
from django.conf import settings
from .serializers import NoteSerializer
import base64


class GetRandomNoteView(views.APIView):
    def get(self, request):
        randomnote = Note.random_note()
        serializer = NoteSerializer(randomnote)
        return JsonResponse(serializer.data)
    


class ImageListView(views.APIView):
    def get(self, request, id):
        images = Attachment.objects.filter(note_id = id)
        image_data = []

        for image in images:
            with open(settings.ATTACHMENTS_DIR + "/" + image.file_path, 'rb') as f:
                image_base64 = base64.b64encode(f.read()).decode('utf-8')
            image_data.append(image_base64)

        return JsonResponse({"images": image_data})