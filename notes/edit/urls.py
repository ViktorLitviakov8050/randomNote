from django.urls import path
from .views import edit

urlpatterns = [
    path('', edit ),
]