# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from random import randint
from i9.models import Question
import csv, os
from django.template import loader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def question(request):
    r = randint(10, 18)
    while(r == StaticVar.last):
        r = randint(10,18)
    StaticVar.last=r

    dataReader = csv.reader(open(os.path.join(BASE_DIR, 'question.csv')), delimiter=',', quotechar='"')
    for row in dataReader:
        if int(row[0]) == r:
            question = Question(id=row[0], content=row[1], result=row[2])
            break
    #question = Question.objects.get(id=r)

    count=0
    arr=[]
    arr.append(int(question.result))
    while (count<3):
        i = randint(0,10)
        if i in arr:
            continue

        arr.append(i)
        count += 1

    arr.sort()

    template = loader.get_template('i10.html')
    context = {
        'content': question.content,
        'v1': arr[0],
        'v2': arr[1],
        'v3': arr[2],
        'v4': arr[3],
        'r': str(question.id),
        'tk': str(question.result),
        'path': '/static/audio/' + str(r) + '.mp3'
    }

    return HttpResponse(template.render(context, request))

def result(request, game):

    if request.method == "POST":
        result = request.POST.get('result')
        tk = request.POST.get('true_key')
        ran = request.POST.get('id')
        # q = Question.objects.get(id=int(ran))

        dataReader = csv.reader(open(os.path.join(BASE_DIR, 'question.csv')), delimiter=',', quotechar='"')
        for row in dataReader:
            if int(row[0]) == int(ran):
                q = Question(id=row[0], content=row[1], result=row[2])
                break

        t = [u'CHÍNH XÁC!', u'QUÁ CHUẨN!', u'RẤT TỐT = ))', u'TUYỆT VỜI ^^', u'CHUẨN LUÔN ; )']
        f = [u'Sai roài :(', u'Không đúng T.T', u'Tính lại đi!']

        if int(result) == int(q.result):
            template = loader.get_template('correct.html')
            context = {
                'game': game+':question',
                'sentence': t[randint(0,4)]
            }

        else:
            template = loader.get_template('incorrect.html')
            context = {
                'key': tk,
                'game': game+':question',
                'sentence': f[randint(0, 2)]
            }

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseBadRequest()

class StaticVar:
    last = 0