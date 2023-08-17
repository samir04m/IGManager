from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-username/', create_username, name='create_username'),
    path('u/<str:username>/', view_username, name='view_username'),
    path('u/<str:username>/del/', delete_username, name='delete_username'),
    path('update-username/<int:username_id>/', update_username, name='update_username'),
    path('change-state/<int:username_id>/', change_state, name='change_state'),
]