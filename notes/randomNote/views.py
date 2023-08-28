from rest_framework import views
from login.models import User 
from django.http import JsonResponse
from django.db import IntegrityError
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


        # import pdb; pdb.set_trace()

        # email = request.POST.get("email")
        # password = request.POST.get("password")
        # try:
        #     user = User.objects.get(email=email, password=password)
        # except User.DoesNotExist:
        #     user = User(email=email, password=password)
        #     try:
        #         user.save()

        #     except IntegrityError:
        #         return JsonResponse({"error:": "Invalid password"}, status=400)
        # return JsonResponse({'token':user.token})
