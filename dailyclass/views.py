from django.shortcuts import render

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
