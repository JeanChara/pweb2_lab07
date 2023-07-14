from xml.dom.minidom import CharacterData
from django.contrib import admin
from .models import Movie,Character
# Register your models here.

admin.site.register(Character)
admin.site.register(Movie)