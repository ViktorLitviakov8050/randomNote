from django.urls import path
from .views import GetRandomNoteView, ImageListView

urlpatterns = [
    path('getrandomnote', GetRandomNoteView.as_view()),
    path('getimages/<int:id>/', ImageListView.as_view()),
]