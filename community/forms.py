from django import forms
from community.models import Question, Answer
from .models import Blog

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
            'board_type' : '게시판타입'
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title' , 'description']