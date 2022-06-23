from django import forms
from community.models import Question, Answer


# from .models import Blog

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
            'board_type': '게시판타입'
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class NoticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

#
# class QuestionForm2(forms.ModelForm):
#     class Meta:
#         model = QnA
#         fields = ('qna_question', 'qna_question_tag', 'user_id')
#
#         widgets = {
#             'qna_question': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
#             'qna_question_tag': forms.Select(attrs={'class': 'form-control'}, choices=QnA.question_tags),
#             'user_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'type': 'hidden'})
#         }
#
#         labels = {
#             'qna_question': '질문이 무엇인가요? ',
#             'qna_question_tag': '어떤 언어에 대한 질문인가요? ',
#         }
