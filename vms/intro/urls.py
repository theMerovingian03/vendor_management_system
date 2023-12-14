from django.urls import path
from .import views

urlpatterns = [
    path('', views.intro_page, name='intro-page')
]