from django.urls import path
from .views import GetRandomNoteView, ImageListView, GetNoteView

urlpatterns = [
    path('getrandomnote', GetRandomNoteView.as_view()),
    path('getimages/<int:id>/', ImageListView.as_view()),
    path('<int:pk>/', GetNoteView.as_view()),
]