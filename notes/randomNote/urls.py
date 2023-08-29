from django.urls import path
from .views import GetRandomNoteView

urlpatterns = [
    path('getrandomnote', GetRandomNoteView.as_view()),
]