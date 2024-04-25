from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_vm/', views.create_vm, name='create_vm'),
    path('vnc/', views.vnc_interface, name='vnc_interface'),
    path('ssh/', views.ssh_view, name='ssh_view'),

    # Add more URLs as needed
]
