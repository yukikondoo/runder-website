from django.urls import path

from . import views
from runder_app import views

# TEMPLATE TAGGING
app_name = 'runder_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.register, name='register'),
    path('special/', views.special, name='special'),
    
]