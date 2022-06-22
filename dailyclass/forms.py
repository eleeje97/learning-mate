from django import forms
from .models import QnA, QnA_answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = ('qna_question', 'qna_question_tag', 'user_id')

        widgets = {
            'qna_question': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'qna_question_tag': forms.Select(attrs={'class': 'form-control'}, choices=QnA.question_tags),
            'user_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'type': 'hidden'})
        }

        labels = {
            'qna_question': '질문이 무엇인가요? ',
            'qna_question_tag': '어떤 언어에 대한 질문인가요? ',
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = ('qna_question', 'qna_question_tag')

        widget = {
            'qna_question': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'qna_question_tag': forms.ChoiceField(choices=QnA.question_tags, required=True),
        }

        labels = {
            'qna_question': '질문이 무엇인가요? ',
            'qna_question_tag': '어떤 언어에 대한 질문인가요? ',
        }