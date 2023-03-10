from django.urls import path
from .views import Guess_Capital

urlpatterns = [
    path('gc/', Guess_Capital)
]