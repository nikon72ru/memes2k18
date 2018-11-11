from django.urls import path

from . import views

urlpatterns = [
    path('fresh', views.fresh, name='fresh'),
    path('upload', views.upload, name='upload'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('get_more', views.get_more, name='get_more'),
    path('hot', views.hot, name='hot'),
    path('relevant', views.relevant, name='relevant'),
    path('finder', views.finder, name='finder'),
]

