from django import forms
from .models import QnA, QnA_answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QnA  # 사용할 모델
        fields = ['qna_question']