from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

# Create your models here.

class Ourbooks( models.Model ):
    bookId = models.CharField(max_length=14, primary_key=True)
    author = models.CharField(max_length=200)
    readingdate = models.CharField(max_length=14)
    category = models.CharField(max_length=14)
    booktitle = models.CharField(max_length=100)
    presentation = models.CharField(max_length=100)
    publisher =  models.CharField(max_length=100)
    statusflag = models.CharField(max_length=5)
    imgindex = models.CharField(max_length=5,default='')
    description = models.TextField(default='')
    def __str__(self):
        return self.booktitle


class Meeting( models.Model ):
    meetingId = models.CharField(max_length=14)
    bookId = models.CharField(max_length=14)
    meetingdate = models.CharField(max_length=14)
    attendants = models.CharField(max_length=100)
    meetingtitle = models.CharField(max_length=100)
    site =  models.CharField(max_length=100)
    photopath =  models.CharField(max_length=200)
    content = models.TextField(default='')
    lastorder = models.TextField(default='')
    def __str__(self):
        return self.meetingtitle

class category( models.Model ):
    categoryCode = models.CharField(max_length=14)
    categoryName = models.CharField(max_length=30)
    def __str__(self):
        return self.categoryName

class Reading( summer_model.Attachment ):
    readId = models.CharField(max_length=30, primary_key=True, default='1')
    title = models.CharField(max_length=30)
    content = summer_fields.SummernoteTextField(default='')
    writer = models.CharField(max_length=30)
    created = models.CharField(max_length=30)
    bookId = models.ForeignKey(Ourbooks, '')
    def __str__(self):
        return str(self.title)+'('+str(self.readId)+')'