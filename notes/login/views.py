from rest_framework import views
from .models import User 
from django.http import JsonResponse
from django.db import IntegrityError



class AuthView(views.APIView):
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            user = User(email=email, password=password)
            try:
                user.save()

            except IntegrityError:
                return JsonResponse({"error:": "Invalid password"}, status=400)
        return JsonResponse({'token':user.token})
