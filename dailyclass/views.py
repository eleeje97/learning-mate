import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from .forms import QuestionForm
from .models import QnA, QnA_answer, ClassMaterial, Quiz


# 학습자료 공유
def classmaterial(request):
    upload_file(request)
    file_list, file_names = fileList(request)
    return render(request, 'dailyclass/classmaterial.html', {'file_list': file_list, 'file_names': file_names})


def upload_file(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print(request.user)
        print(request.POST['comment'])
        if request.FILES:
            # material = ClassMaterial(comment=request.POST['comment'], file_name=str(request.FILES['uploaded_file']), file_url=request.FILES['uploaded_file'], user_id=request.user)
            material = ClassMaterial(comment=request.POST['comment'],
                                     file_url=request.FILES['uploaded_file'], user_id=request.user)
            print('파일:', request.FILES['uploaded_file'])
            print(material)
            print(request.FILES['uploaded_file'].content_type)
            material.save()


def fileList(request):
    file_list = ClassMaterial.objects.all()
    file_names = []
    for i in file_list:
        file_names.append(i.get_filename())
    return file_list, file_names


class FileDownloadView(SingleObjectMixin, View):
    queryset = ClassMaterial.objects.all()

    def get(self, request, file_id):
        object = self.get_object(file_id)

        file_path = object.file_url.path
        # file_type = object.content_type  # django file object에 content type 속성이 없어서 따로 저장한 필드
        fs = FileSystemStorage(file_path)
        response = FileResponse(fs.open(file_path, 'rb')) #content_type=file_type
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



# Quiz
lst=[]
def home(request):
    return render(request, 'quiz.html')

def quiz(request):
    template_name = 'dailyclass/quiz.html'
    obj = Quiz.objects.all()
    return render(request, template_name, {"obj":obj})


# 질문있어요!
def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

  
def test_view(request):
    return render(request, 'dailyclass/test.html',)


def question_list(request):
    questions = QnA.objects.all().order_by('-pk')

    return render(request,
                  'dailyclass/question_list.html',
                  {
                      'questions':questions,
                  })


def single_question_page(request, qna_id):
    question = QnA.objects.get(qna_id=qna_id)

    return render(request,'dailyclass/question/single_question_page.html',
                  {'question':question,})


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
