import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dailyclass:single_question_page', kwargs={'pk': self.pk})

class QnA(models.Model):
    question_tags = [('R', 'R'),
                     ('Python', 'Python'),
                     ('HTML', 'HTML'),
                     ('CSS', 'CSS'),
                     ('JavaScript', 'JavaScript'),
                     ('Django', 'Django'),
                     ('Others', 'Others'),
                     ]
    qna_id = models.BigAutoField(primary_key=True)
    qna_question = RichTextUploadingField(blank=True, null=True)
    qna_question_tag = models.CharField(max_length=10, choices=question_tags)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    # on_delete=models.CASCADE의 의미는 이 유저의 계정이 삭제될 경우 질문도 함께 삭제된다는 의미


    def __str__(self):
        return f'[{self.qna_id}] {self.qna_question}'

    def get_absolute_url(self):
        return reverse('dailyclass:single_question_page', kwargs={'pk': self.pk})


class QnA_answer(models.Model):
    answer_id = models.BigAutoField(primary_key=True)
    qna_id = models.ForeignKey(QnA, related_name="answers", on_delete=models.CASCADE, db_column='qna_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    qna_answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.qna_id, self.user_id)


class Quiz(models.Model):
    quiz_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, db_column='user_id')
    quiz_question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.IntegerField()

class result(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE,db_column='quiz_id')
    answer_num = models.IntegerField()
    checking = models.BooleanField()



class ClassMaterial(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    file_url = models.FileField('uploaded_file', upload_to='class_material/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    comment = models.CharField(max_length=500, null=True, blank=True)
    file_type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)

    def get_filename(self):
        return os.path.basename(self.file_url.name)
