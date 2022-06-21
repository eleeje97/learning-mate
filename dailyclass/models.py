import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User


class QnA(models.Model):
    qna_id = models.BigAutoField(primary_key=True)
    qna_question = RichTextUploadingField(blank=True, null=True)
    qna_question_tag = models.CharField(max_length=50, default="others")
    #qna_question = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img_path = models.TextField(null=True)  # img가 없을수도 있으므로 null=True
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    # on_delete=models.CASCADE의 의미는 이 유저의 계정이 삭제될 경우 질문도 함께 삭제된다는 의미

    def __str__(self):
        return f'[{self.qna_id}] {self.qna_question}'

    def get_absolute_url(self):
        return f'/dailyclass/question/{self.qna_id}'


class QnA_answer(models.Model):
    answer_id = models.BigAutoField(primary_key=True)
    qna_id = models.ForeignKey(QnA, on_delete=models.CASCADE, db_column='qna_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    qna_answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Quiz(models.Model):
    quiz_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50)
    quiz_question = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class QuizAnswer(models.Model):
    quiz_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50)
    quiz_answer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class ClassMaterial(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    file_url = models.FileField('uploaded_file', upload_to='class_material/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    comment = models.CharField(max_length=500, null=True, blank=True)
    file_type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)

    def get_filename(self):
        return os.path.basename(self.file_url.name)
