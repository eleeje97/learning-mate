from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import QuestionForm
from .models import QnA, QnA_answer

def classmaterial(request):
    return render(request, 'dailyclass/classmaterial.html')


def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

def upload_file(request):
    if request.method == "POST":
        print(request.FILES)
        if request.FILES:
            print('파일:',request.FILES['uploaded_file'])
    return render(request, 'dailyclass/classmaterial.html')
  
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
