from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class StateResource(resources.ModelResource):
    class Meta:
        model = State

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'order',)
    resource_class = StateResource

class UsernameResource(resources.ModelResource):
    class Meta:
        model = Username

class UsernameAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['username']
    list_display = ('username', 'state',)
    resource_class = UsernameResource

admin.site.register(State, StateAdmin)
admin.site.register(Username, UsernameAdmin)