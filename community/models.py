from django.db import models
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from learningmate import settings


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    board_type = models.CharField(max_length=6)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     description = RichTextUploadingField(blank=True,null=True)
#     body = models.TextField()
# #    username = models.CharField(max_length=50)