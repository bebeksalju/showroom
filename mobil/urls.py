from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_mobil, name='daftar_mobil'),
    path('tambah/', views.tambah_mobil, name='tambah_mobil'),
    path('<int:mobil_id>/', views.detail_mobil, name='detail_mobil'),
    path('<int:mobil_id>/service/', views.tambah_service, name='tambah_service'),
    path('<int:mobil_id>/hapus/', views.hapus_mobil, name='hapus_mobil'),
    path('<int:mobil_id>/edit/', views.edit_mobil, name='edit_mobil'),
]