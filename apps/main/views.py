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
            messages.info(request, 'Username is currently in "{}"'.format(username.state.name), extra_tags='info')
        else:
            if igUsername:
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
    if len(path_parts) == 1:
        return path_parts[0]
    else:
        return path_parts[1]

def change_state(request, username_id):
    username = get_object_or_404(Username, id=username_id)
    nState = username.state.order
    username.state = get_object_or_404(State, order=nState+1)
    username.save()
    return redirect(request.META.get('HTTP_REFERER'))

def view_username(request, username):
    username = get_object_or_404(Username, username=username)
    states = State.objects.all()
    return render(request, 'main/view_username.html', {'username':username, 'states':states})

def update_username(request, username_id):
    if request.method == 'POST':
        username = get_object_or_404(Username, id=username_id)
        updated = False
        if int(request.POST.get('state')) != username.state.id:
            username.state = State.objects.get(id=int(request.POST.get('state')))
            updated = True
        if request.POST.get('info') != username.info:
            print("entro ------")
            username.info = request.POST.get('info')
            updated = True
        if updated:
            username.save()
            messages.success(request, 'Username updated', extra_tags='success')
    return redirect(request.META.get('HTTP_REFERER'))

def delete_username(request, username):
    username = get_object_or_404(Username, username=username)
    username.delete()
    uname = username.username
    messages.success(request, 'Username "{}" was removed'.format(uname), extra_tags='success')
    return redirect('main:home')

