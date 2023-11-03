from rest_framework import views
from .models import Note, Attachment
from django.http import JsonResponse
from django.conf import settings
from .serializers import NoteSerializer
import base64
from rest_framework.generics import RetrieveAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(responses={200: NoteSerializer}, summary='Get random note information', description="Get randomly one of the notes")
class GetRandomNoteView(views.APIView):
    def get(self, request):
        randomnote = Note.random_note()
        serializer = NoteSerializer(randomnote)
        return JsonResponse(serializer.data)


@extend_schema(responses={200: NoteSerializer}, summary='Get specific note by its id')
class GetNoteView(RetrieveAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects


@extend_schema(summary='Get list of images by note id', description='Get list of images in base64 format')
class ImageListView(views.APIView):
    def get(self, request, id):
        images = Attachment.objects.filter(note_id=id)
        image_data = []

        for image in images:
            with open(settings.ATTACHMENTS_DIR + "/" + image.file_path, 'rb') as f:
                image_base64 = base64.b64encode(f.read()).decode('utf-8')
                full_image_base64 = f"data:image/png;base64,{image_base64}"
            image_data.append(full_image_base64)
        return JsonResponse({"images": image_data})
