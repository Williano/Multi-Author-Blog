from django.contrib import admin
from .models import Post


# Registers blog app the django admin backend.
admin.site.register(Post)