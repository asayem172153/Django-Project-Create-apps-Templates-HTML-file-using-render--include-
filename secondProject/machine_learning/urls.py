from django.urls import path
from . import views

urlpatterns = [
    path('su/', views.supervised),
    path('un/', views.unsupervised),
]
