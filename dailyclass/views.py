from django.shortcuts import render
#from . models import Post

def classmaterial(request):

    #posts = Post.objects.all()

    return render(
        request,
        'dailyclass/classmaterial.html',
        # {
        #     'posts': posts,
        # }
    )


def question_form(request):
    return render(request, 'dailyclass/question_form.html',)

def test_view(request):
    return render(request, 'dailyclass/test.html',)
