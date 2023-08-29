from django.urls import path
from .views import AuthView

urlpatterns = [
    path('', AuthView.as_view()),
]