import datetime
import os

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import QnA, QnA_answer, ClassMaterial, Quiz, result
from .forms import QuestionForm, EditForm



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
def quiz(request):
    quiz = Quiz.objects.get(pk=1)

    return render(request, 'dailyclass/quiz/quiz.html',{"quiz":quiz})

def result(request):
    res = result.object.all()
    return render(request, 'dailyclass/quiz/result.html', {"res":res})

# 질문있어요!
def test_view(request):
    return render(request, 'dailyclass/test.html',)


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
