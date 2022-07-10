from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dailyclass/classmaterial')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def forgot_password(request):
    return render(request, 'accounts/auth-forgot-password.html')


@login_required(login_url='accounts:login')
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dailyclass:classmaterial')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/profile.html', {'form': form})
