from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('serve_file/<str:file_path>/', views.serve_file, name='serve_file'),
    path('create_zip_and_download/', views.create_zip_and_download, name='create_zip_and_download'),
]
