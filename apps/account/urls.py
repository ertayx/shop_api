from django.urls import path
from views import *

urlpatterns = [
    path('register/', RegistrationsView.as_view()),
    path('activate/', ActivationView.as_view()),
]