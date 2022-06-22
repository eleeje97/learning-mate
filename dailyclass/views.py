import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView, CreateView


from .forms import QuestionForm
from .models import QnA, QnA_answer, ClassMaterial, Quiz, result

#여기서 전역변수로 지정해주겠습니다

# 학습자료 공유
def classmaterial(request):
    upload_file(request)
    file_list = fileList(request)
    return render(request, 'dailyclass/classmaterial.html', {'file_list': file_list})


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


def fileList(request):
    file_list = ClassMaterial.objects.all()
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
    quiz = Quiz.objects.filter(quiz_id=request.POST['quiz_id'])
    return render(request, 'dailyclass/quiz/quiz.html',{"quiz":quiz})

def result(request):
    res = result.object.all()
    return render(request, 'dailyclass/quiz/result.html',) #{"res":res})

# def score(request):
#     num = 1
#     if request.POST:
#         num = int(request.POST['answer_num'])
#         if quiz.answer == num:  #여기서 인덱스를 어땋게 확인할까
#             checklst=[]
#             checklst += result.checking() #boolean?????

# 질문있어요!
def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

  
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



class single_question_page(DetailView):
    model = QnA
    template_name = 'dailyclass/question/single_question_page.html'

    def get_object(self, queryset=None):
        object = get_object_or_404(QnA, pk=self.kwargs['qna_id'])
        return object

class AddQuestionView(CreateView):
    model = QnA
    template_name = 'dailyclass/question_form.html'
    fields = '__all__'

def question_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            qna = form.save(commit=False)
            qna.user_id = request.user
            qna.qna_question = request.POST['qna_question']
            qna.date = timezone.now()
            qna.save()
            return redirect('dailyclass:question_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'dailyclass/question_form.html', context)
