from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-username/', create_username, name='create_username'),
    path('change-state/<int:username_id>/', change_state, name='change_state'),
]