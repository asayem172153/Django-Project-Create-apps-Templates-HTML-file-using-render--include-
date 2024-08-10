from django.urls import path
from . import views

urlpatterns = [
    path('jv/', views.java),
    path('pt/',views.python)
]
