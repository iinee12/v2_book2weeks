from django.contrib import admin
from .models import Ourbooks
from .models import Meeting
from .models import category

# Register your models here.
admin.site.register(Ourbooks)
admin.site.register(Meeting)
admin.site.register(category)