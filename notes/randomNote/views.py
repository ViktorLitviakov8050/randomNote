from rest_framework import views
from login.models import User 
from .models import Note 
from django.http import JsonResponse
from uuid import UUID
from notes.cryptographer import Cryptographer
from django.conf import settings
from .serializers import NoteSerializer

class GetRandomNoteView(views.APIView):
    def get(self, request):
        randomnote = Note.random_note()
        serializer = NoteSerializer(randomnote)
        return JsonResponse(serializer.data)