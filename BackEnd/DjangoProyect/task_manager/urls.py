from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create-task'), 
    path('tasks/<int:pk>/', views.update_task, name='update-task'),  
]