from django import forms
from .models import QnA, QnA_answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = ('qna_question', 'qna_question_tag', 'user_id')

        widget = {
            'qna_question': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'qna_question_tag': forms.ChoiceField(choices=QnA.question_tags, required=True),
            # 'img_path': forms.TextInput(attrs={'class': 'form-control'}),
            'user_id': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'qna_question': '질문이 무엇인가요? ',
            'qna_question_tag': '질문에 맞는 태그는요? ',
            # 'img_path': '이미지 경로는요? ',
            'user_id': '누가 작성하셨나요? ',
        }