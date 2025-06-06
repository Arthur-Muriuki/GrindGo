from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.routine_list, name='routine_list'),  # after login
]
path('create/', views.routine_create, name='routine_create'),
path('update/<int:pk>/', views.routine_update, name='routine_update'),
path('delete/<int:pk>/', views.routine_delete, name='routine_delete'),
