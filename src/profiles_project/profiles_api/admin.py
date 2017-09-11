from django.contrib import admin

# New changes
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
