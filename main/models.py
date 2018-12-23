from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.contrib.auth.models import User

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
    discuss = models.TextField(default='')
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
    newMemberYN = models.CharField(max_length=2, default='')
    lastorder = models.CharField(max_length=200, default='')
    content = models.TextField(default='')
    
    def __str__(self):
        return self.meetingtitle

class category( models.Model ):
    categoryCode = models.CharField(max_length=14)
    categoryName = models.CharField(max_length=30)
    def __str__(self):
        return self.categoryName

class Reading( summer_model.Attachment ):
    readId = models.CharField(max_length=30, primary_key=True, default='1')
    title = models.CharField(max_length=50)
    content = summer_fields.SummernoteTextField(default='')
    writer = models.CharField(max_length=30)
    created = models.CharField(max_length=30)
    bookId = models.ForeignKey(Ourbooks, '')
    def __str__(self):
        return str(self.title)+'('+str(self.readId)+')'


class sentence( models.Model ):
    senId = models.CharField(max_length=30, primary_key=True)
    bookId = models.ForeignKey(Ourbooks, '')
    senContent = models.TextField(default='')
    senWriter = models.CharField(max_length=30)
    created = models.CharField(max_length=30)
    def __str__(self):
        return str(self.bookId)+'('+str(self.senWriter)+')'+'('+str(self.senId)+')'


class petercatSentence( models.Model ):
    senId = models.CharField(max_length=30, primary_key=True)
    bookName = models.CharField(max_length=100)
    senContent = models.TextField(default='')
    senWriter = models.CharField(max_length=30)
    register = models.CharField(max_length=30)
    created = models.CharField(max_length=30)

class starScore( models.Model ):
    scoreId = models.CharField(max_length=30, primary_key=True)
    bookId = models.ForeignKey(Ourbooks, '')
    scoreComment = models.TextField(default='')
    scoreStar = models.CharField(max_length=30)
    scoreWriter = models.CharField(max_length=30)
    created = models.CharField(max_length=30)
    scoreDuble = models.CharField(max_length=30, default='')
    def __str__(self):
        return str(self.bookId)+'('+str(self.scoreWriter)+')'+'('+str(self.scoreId)+')'



class Wishbooks( models.Model ):
    wishId = models.CharField(max_length=30, primary_key=True)
    bookId = models.CharField(max_length=100)
    register = models.CharField(max_length=100)
    wishbooktitle =  models.CharField(max_length=100)
    ourbookflag = models.CharField(max_length=5)
    reason = models.TextField(default='')
    created = models.CharField(max_length=30)
    imgindex = models.CharField(max_length=30, default='')
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.wishbooktitle
        
    @property
    def total_likes(self):
        return self.likes.count() #likes 컬럼의 값의 갯수를 센다

class readingReplys ( models.Model):
    replyId = models.CharField(max_length=30, primary_key=True)
    readId = models.ForeignKey(Reading, '')
    replyContent = models.TextField(default='')
    replyWriter = models.CharField(max_length=30)
    created = models.CharField(max_length=30)
    def __str__(self):
        return str(self.readId)+'('+str(self.replyWriter)+')'+'('+str(self.replyId)+')'