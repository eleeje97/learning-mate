from django.db import models

from accounts.models import User


class QnA(models.Model):
    qna_id = models.BigAutoField(primary_key=True)
    qna_question = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img_path = models.TextField(null=True)  # img가 없을수도 있으므로 null=True
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    # on_delete=models.CASCADE의 의미는 이 유저의 계정이 삭제될 경우 질문도 함께 삭제된다는 의미


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