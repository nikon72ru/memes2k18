from django.urls import path

from . import views

urlpatterns = [
    path('fresh', views.fresh, name='fresh'),
    path('upload', views.upload, name='upload'),
]

