from django.urls import path
from . import views

urlpatterns = [
    path('',views.database),
    path('sq/', views.sql),
]
