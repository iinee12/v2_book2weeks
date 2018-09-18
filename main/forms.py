from django_summernote import fields as summer_fields
from .models import Reading, sentence, starScore, Wishbooks
from django.contrib.auth.models import User
from django import forms


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Reading
        widgets = {
            'readId': forms.TextInput({'type':'hidden', 'id':'readIdforupdate'})
        }
        fields = ('content', 'title', 'bookId', 'readId' )

class wishbookForm(forms.ModelForm):
    
    class Meta:
        model = Wishbooks
        widgets = {
            'wishbooktitle': forms.TextInput({'type':'hidden', 'id':'wishbooktitle'}),
            'bookId': forms.TextInput({'type':'hidden', 'id':'wishbookId'}),
            'reason': forms.Textarea({'type':'hidden', 'id':'wishbookReason'})
        }
        fields = ('reason', 'wishbooktitle', 'bookId' )

class SentenceForm(forms.ModelForm):
    
    class Meta:
        model = sentence
        widgets = {
            'bookId': forms.TextInput({'type':'hidden', 'id':'idSenForBookId'}),
            'senContent': forms.Textarea({'rows':'5', 'class':'sentenceTextField'})
        }
        fields = ('senContent', 'bookId')

class SoreForm(forms.ModelForm):
    
    class Meta:
        model = starScore
        widgets = {
            'bookId': forms.TextInput({'type':'hidden', 'id':'idScoreForBookId'}),
            'scoreStar': forms.TextInput({'type':'hidden', 'id':'idScoreForScoreStar'}),
            'scoreComment': forms.Textarea({'rows':'3', 'class':'scoreTextField'})
        }
        fields = ('scoreComment', 'bookId', 'scoreStar' )

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput({'placeholder': 'Enter ID'}),
            'password': forms.TextInput({'placeholder': 'Enter password','type':'password'})
        }
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.