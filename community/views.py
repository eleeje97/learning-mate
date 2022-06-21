from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Question, Answer ,User
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q



def notice(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date').filter(board_type=1)
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw)  # 답변 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'notice/question_list.html', context)


def information(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date').filter(board_type=2)
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw)  # 답변 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'information/question_list.html', context)


def chat(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date').filter(board_type=3)
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw)  # 답변 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'community/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'community/question_detail.html', context)


@login_required(login_url='accounts:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('community:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'community/question_detail.html', context)


@login_required(login_url='accounts:login')
def notice_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.create_date = timezone.now()
            question.board_type = request.POST['board_type']
            question.save()
            return redirect('community:notice')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'notice/question_form.html', context)


@login_required(login_url='accounts:login')
def information_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.create_date = timezone.now()
            question.board_type = request.POST['board_type']
            question.save()
            return redirect('community:information')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'information/question_form.html', context)


@login_required(login_url='accounts:login')
def question_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.create_date = timezone.now()
            question.board_type = request.POST['board_type']
            question.save()
            return redirect('community:chat')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'community/question_form.html', context)


@login_required(login_url='accounts:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('community:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('community:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'community/question_form.html', context)


@login_required(login_url='accounts:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('community:detail', question_id=question.id)
    question.delete()
    return redirect('community:chat')


@login_required(login_url='accounts:login')
def information_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('community:detail', question_id=question.id)
    question.delete()
    return redirect('community:information')


@login_required(login_url='accounts:login')
def notice_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('community:detail', question_id=question.id)
    question.delete()
    return redirect('community:notice')


@login_required(login_url='accounts:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('community:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('community:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'community/answer_form.html', context)


@login_required(login_url='accounts:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.user:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('community:detail', question_id=answer.question.id)

