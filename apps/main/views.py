from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import *

from urllib.parse import urlparse, parse_qs

def home(request):
    states = State.objects.all()
    return render(request, 'main/home.html', {'states':states})

def create_username(request):
    if request.method == 'POST':
        igUsername = getUsernameFromUrl(request.POST.get('url'))
        username = Username.objects.filter(username=igUsername).first()
        if username:
            messages.info(request, 'Username already exists', extra_tags='info')
        else:
            try:
                username = Username(
                    username = igUsername,
                    state = State.objects.get(order=1)
                )
                username.save()
                messages.success(request, 'Username saved', extra_tags='success')
            except Exception as ex:
                messages.error(request, 'Failed to add username', extra_tags='error')
    return redirect(request.META.get('HTTP_REFERER'))

def getUsernameFromUrl(url:str) -> str:
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split("/")
    username = path_parts[-1]
    return username

def change_state(request, username_id):
    username = get_object_or_404(Username, id=username_id)
    nState = username.state.order
    username.state = get_object_or_404(State, order=nState+1)
    username.save()
    return redirect(request.META.get('HTTP_REFERER'))

