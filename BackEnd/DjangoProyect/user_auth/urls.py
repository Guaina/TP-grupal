from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  
from . import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'), 
    path('register/', views.RegisterView.as_view(), name='register'), 
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]
