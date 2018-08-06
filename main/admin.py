from django.contrib import admin
from .models import Ourbooks, Meeting, category, Reading

# Register your models here.
admin.site.register(Ourbooks)
admin.site.register(Meeting)
admin.site.register(category)
admin.site.register(Reading)