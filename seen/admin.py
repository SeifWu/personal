from django.contrib import admin

# Register your models here.
from .models import Category, WatchedObject, Tag

admin.site.register(Category)
admin.site.register(WatchedObject)
admin.site.register(Tag)
