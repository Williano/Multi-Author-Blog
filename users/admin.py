# Third party imports.
from django.contrib import admin

# Local application imports.
from .models import Profile

# Registers Profile app at the admin backend.
admin.site.register(Profile)
