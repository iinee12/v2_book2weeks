from django.contrib import admin
from .models import Ourbooks, Meeting, category, Reading, sentence, starScore, Wishbooks

# Register your models here.
admin.site.register(Ourbooks)
admin.site.register(Meeting)
admin.site.register(category)
admin.site.register(Reading)
admin.site.register(sentence)
admin.site.register(starScore)
admin.site.register(Wishbooks)
