import datetime
import os

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import QnA, QnA_answer, ClassMaterial, Quiz
from .forms import QuestionForm, EditForm, CommentForm, EditCommentForm
#from .models import Question, Answer, User
from django.http import HttpResponseNotAllowed
#from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q



# 학습자료 공유
@login_required(login_url='accounts:login')
def classmaterial(request):
    if request.GET.get('date') is None:
        date = datetime.datetime.now().date()
    else:
        date = datetime.datetime.strptime(request.GET.get('date'), "%Y-%m-%d").date()

    upload_file(request)
    file_list = fileList(request, date)

    return render(request, 'dailyclass/classmaterial.html', {'file_list': file_list, 'date': date})


def upload_file(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print(request.user)
        print(request.POST['comment'])
        if request.FILES:
            material = ClassMaterial(comment=request.POST['comment'], file_name=str(request.FILES['uploaded_file']), file_type=request.FILES['uploaded_file'].content_type, file_url=request.FILES['uploaded_file'], user_id=request.user)
            print('파일:', request.FILES['uploaded_file'])
            print(material)
            print(request.FILES['uploaded_file'].content_type)
            material.save()


def fileList(request, date):
    # file_list = ClassMaterial.objects.all()
    file_list = ClassMaterial.objects.filter(date__range=[date, date + datetime.timedelta(days=1)])
    return file_list


class FileDownloadView(SingleObjectMixin, View):
    queryset = ClassMaterial.objects.all()

    def get(self, request, file_id):
        object = self.get_object(file_id)

        file_path = object.file_url.path
        file_type = object.file_type
        fs = FileSystemStorage(file_path)
        response = FileResponse(fs.open(file_path, 'rb'), content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename={object.get_filename()}'

        return response

    def get_object(self, queryset=None):
        object = get_object_or_404(ClassMaterial, id=self.kwargs['file_id'])
        return object


def delete_file(request, file_id):
    file = get_object_or_404(ClassMaterial, pk=file_id)
    file_url = os.path.join(settings.MEDIA_ROOT, str(file.file_url))
    os.remove(file_url)
    file.delete()
    return redirect('dailyclass:classmaterial')


#퀴즈

def quiz_home(request):
    return render(request, 'dailyclass/quiz/quiz_home.html')

def quiz(request):
    quiz_id=request.GET['quiz_id']
    quiz = Quiz.objects.filter(pk=quiz_id)
    return render(request, 'dailyclass/quiz/quiz.html',{'quiz':quiz})

# def result(request):
#     res = result.object.all()
#     return render(request, 'dailyclass/quiz/result.html',) #{"res":res})

# def score(request):
#     num = 1
#     if request.POST:
#         num = int(request.POST['answer_num'])
#         if quiz.answer == num:  #여기서 인덱스를 어땋게 확인할까
#             checklst=[]
#             checklst += result.checking() #boolean?????

# 질문있어요!
def test_view(request):
    return render(request, 'dailyclass/test.html',)

def score(request):
    num = 1
    if request.POST:
        num = int(request.POST['answer_num'])
        if quiz.answer == num:  #여기서 인덱스를 어땋게 확인할까
            checklst=[]
            #checklst += result.checking() #boolean?????


class question_list(ListView):
    model = QnA
    template_name = 'dailyclass/question_list.html'
    ordering = ['-pk']

    # 검색 기능 완성!
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(qna_question__icontains = query)
        return qs



class single_question_page(DetailView):
    model = QnA
    template_name = 'dailyclass/question/single_question_page.html'

    # def get_object(self, queryset=None):
    #     object = get_object_or_404(QnA, pk=self.kwargs['qna_id'])
    #     return object

class AddQuestionView(CreateView):
    model = QnA
    form_class = QuestionForm
    template_name = 'dailyclass/question/question_form.html'
    # fields = '__all__'
    # fields = ('qna_question', 'qna_question_tag')


class AddCommentView(CreateView):
    model = QnA_answer
    form_class = CommentForm
    template_name = 'dailyclass/question/add_comments.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.qna_id = self.kwargs['pk']
        return super().form_valid(form)


    success_url = '/dailyclass/question/{qna_id}'



class UpdateQuestionView(UpdateView):
    model = QnA
    form_class = EditForm
    template_name = 'dailyclass/question/edit/question_update_form.html'
    # fields = ['qna_question', 'qna_question_tag']


class UpdateAnswerView(UpdateView):
    model = QnA_answer
    form_class = EditCommentForm
    template_name = 'dailyclass/question/edit/edit_comments.html'


class DeleteQuestionView(DeleteView):
    model = QnA
    template_name = 'dailyclass/question/edit/delete_question.html'
    success_url = reverse_lazy('dailyclass:question_list')


class DeleteAnswerView(DeleteView):
    model = QnA_answer
    template_name = 'dailyclass/question/edit/delete_answer.html'
    success_url = '/dailyclass/question/{qna_id}'
