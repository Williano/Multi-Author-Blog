from django.contrib import admin
from .models import Profile

# Registers Profile app at the admin backend.
admin.site.register(Profile)
