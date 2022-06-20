from django.shortcuts import render
from dailyclass.models import ClassMaterial


def classmaterial(request):
    return render(request, 'dailyclass/classmaterial.html')


def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

  
def test_view(request):
    return render(request, 'dailyclass/test.html',)


def upload_file(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print(request.user)
        print(request.POST['comment'])
        if request.FILES:
            material = ClassMaterial(comment=request.POST['comment'], file_url=request.FILES['uploaded_file'], user_id=request.user)
            print('파일:', request.FILES['uploaded_file'])
            print(material)
            material.save()

    return render(request, 'dailyclass/classmaterial.html')
