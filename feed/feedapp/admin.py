from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Report

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post) # first created in models then makemigrations and migrate;: and registered here
admin.site.register(Report) # first created in models then makemigrations and migrate;: and registered here - move on to views


