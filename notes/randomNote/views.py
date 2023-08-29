from rest_framework import views
from login.models import User 
from django.http import JsonResponse
from uuid import UUID


class GetRandomNoteView(views.APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        try:
            token = UUID(token.replace('Bearer ' , ''))
            user = User.objects.get(token=token)
        except (ValueError, User.DoesNotExist):
            return JsonResponse({"error:": "Invalid token"}, status=401)
        return JsonResponse({"note": "randomnote"})