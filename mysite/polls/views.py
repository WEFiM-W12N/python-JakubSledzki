from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    return HttpResponse("Pytania.")
# Create your views here.

    
def detail(request, question_id):
    return HttpResponse("Pytanie nr.%s." % question_id)

    
def results(request, question_id):
    response = "Wyniki pytania nr.%s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("głosujesz na pytanie nr.%s." % question_id)