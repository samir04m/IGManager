from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *


def home(request):
    return render(request, 'main/home.html')