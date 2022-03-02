from django.urls import path

from . import views
from runder_app import views

# TEMPLATE TAGGING
app_name = 'runder_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    
]