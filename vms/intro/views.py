from django.shortcuts import render
from .models import APIs
# Create your views here.

def intro_page(request):
    api_info = APIs.objects.all()
    return render(request, 'intro.html', {'api_info':api_info})