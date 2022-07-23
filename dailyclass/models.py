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
    qna = models.ForeignKey(QnA, related_name="answers", on_delete=models.CASCADE, db_column='qna')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    qna_answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user_id}::{self.qna_answer}'

    def get_absolute_url(self):
        return reverse('dailyclass:single_question_page', kwargs={'pk': self.qna.pk})


class Quiz(models.Model):
    quiz_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, db_column='user_id')
    quiz_title = models.CharField(max_length=200)
    quiz_content = models.TextField()
    date = models.DateTimeField()


class QuizAnswer(models.Model):
    answer_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, db_column='quiz_id')
    answer_content = models.TextField()
    date = models.DateTimeField()


class ClassMaterial(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    file_url = models.FileField('uploaded_file', upload_to='class_material/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    comment = models.CharField(max_length=500, null=True, blank=True)
    file_type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)

    def get_filename(self):
        return os.path.basename(self.file_url.name)
