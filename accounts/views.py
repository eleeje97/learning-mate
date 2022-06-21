from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm


def signup(request):
    if request.method == "POST":
        print(request.POST)
        # 회원가입에 필요한 코드를 작성한다.
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dailyclass/classmaterial')
    else:
        # 회원가입 폼을 응답한다.
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def forgot_password(request):
    return render(request, 'accounts/auth-forgot-password.html')
