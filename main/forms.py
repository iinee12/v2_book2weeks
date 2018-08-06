from django_summernote import fields as summer_fields
from .models import Reading
from django import forms

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Reading
        fields = ('content', 'title', )
