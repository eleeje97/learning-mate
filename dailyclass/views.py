from django.shortcuts import render
from .models import Quiz

lst=[]
def classmaterial(request):
    return render(request,'dailyclass/classmaterial.html')

def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

def home(request):
    return render(request, 'quiz.html')

def quiz(request):
    template_name = 'dailyclass/quiz.html'
    obj = Quiz.objects.all()
    return render(request, template_name, {"obj":obj})



