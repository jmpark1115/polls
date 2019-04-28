from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

# Create your tests here.
from polls.models import Question, Choice
from django.utils import timezone

def test1(request):
    # q = Question(question_text = "What's new?", pub_date= timezone.now() )
    # print(result)

    q = Question.objects.all()
    print(q)

    q = Question.objects.filter(question_text__startswith="What")
    print(q)

    q = Question.objects.get(pk=1)
    q.question_text = "What's your favorite sports?"
    print(q)

    # q.question_text = "What's your home town?"
    # print(q.save)

    return HttpResponse('success')