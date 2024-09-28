from django.shortcuts import render
from .forms import QuestionForm
from .models import Question


def question_create(request):
    if request.method == "POST":
        authors = QuestionForm(request.POST)
        if authors.is_valid():
            authors.save()
            return render(request, 'question_success.html')
    form = {'form': QuestionForm}
    return render(request, 'question_form.html', form)


def question_list(request):
    questions = Question.objects.all()
    ctx = {'questions': questions}

    return render(request, 'question_list.html', ctx)
