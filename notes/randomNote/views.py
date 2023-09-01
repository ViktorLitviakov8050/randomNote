from rest_framework import views
from login.models import User 
from django.http import JsonResponse
from uuid import UUID
from login.cryptographer import Cryptographer
from django.conf import settings


class GetRandomNoteView(views.APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        try:
            token = UUID(token.replace('Bearer ' , ''))
            user = User.objects.get(token=token)
        except (ValueError, User.DoesNotExist):
            return JsonResponse({"error:": "Invalid token"}, status=401)
        key = settings.SECRET_KEY
        decrypt_pass = Cryptographer(key).decrypt(user.password)
        print(user.email)
        print(decrypt_pass)
        return JsonResponse({"note": "randomnote"})