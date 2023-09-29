

from django.contrib import admin
from .models import Person,User_datas

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')



@admin.register(User_datas)
class User_dataAdmin(admin.ModelAdmin):
    list_display = ('username', 'mail','password',)