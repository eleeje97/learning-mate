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

from .models import QnA, QnA_answer, ClassMaterial, Quiz, result
from .forms import QuestionForm, EditForm


#여기서 전역변수로 지정해주겠습니다

# 학습자료 공유
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
    quiz = Quiz.objects.filter(pk=1)#(quiz_id=request.POST['quiz_id'])
    return render(request, 'dailyclass/quiz/quiz.html')#{"quiz":quiz})

def result(request):
    res = result.object.all()
    return render(request, 'dailyclass/quiz/result.html',) #{"res":res})

def score(request):
    num = 1
    if request.POST:
        num = int(request.POST['answer_num'])
        if quiz.answer == num:  #여기서 인덱스를 어땋게 확인할까
            checklst=[]
            checklst += result.checking() #boolean?????

# 질문있어요!
def test_view(request):
    return render(request, 'dailyclass/test.html',)

def score(request):
    num = 1
    if request.POST:
        num = int(request.POST['answer_num'])
        if quiz.answer == num:  #여기서 인덱스를 어땋게 확인할까
            checklst=[]
            checklst += result.checking() #boolean?????


class question_list(ListView):
    model = QnA
    template_name = 'dailyclass/question_list.html'
    ordering = ['-pk']



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





class UpdateQuestionView(UpdateView):
    model = QnA
    form_class = EditForm
    template_name = 'dailyclass/question/edit/question_update_form.html'
    # fields = ['qna_question', 'qna_question_tag']



class DeleteQuestionView(DeleteView):
    model = QnA
    template_name = 'dailyclass/question/edit/delete_question.html'
    success_url = reverse_lazy('dailyclass:question_list')
#
# def information(request):
#     page = request.GET.get('page', '1')  # 페이지
#     kw = request.GET.get('kw', '')
#     question_list = QnA.objects.order_by('-create_date').filter(board_type=2)
#     if kw:
#         question_list = question_list.filter(
#             Q(subject__icontains=kw) |  # 제목 검색
#             Q(content__icontains=kw) |  # 내용 검색
#             Q(answer__content__icontains=kw)  # 답변 검색
#         ).distinct()
#     paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)
#     context = {'question_list': page_obj, 'page': page, 'kw': kw}
#     return render(request, 'dailyclass/question_list.html', context)