# -*- coding: utf-8 -*-
from random import randint
from models import Question
import csv, os
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def content(request):
    template = loader.get_template('content.html')
    return HttpResponse(template.render(request))

def question(request):

    r = randint(1, 9)
    while (r == StaticVar.last):
        r = randint(1,9)
    StaticVar.last = r
    # print 'LAST = {}'.format(StaticVar.last)

    dataReader = csv.reader(open(os.path.join(BASE_DIR, 'question.csv')), delimiter=',', quotechar='"')
    for row in dataReader:
        if int(row[0]) == r:
            question = Question(id=row[0], content=row[1], result=row[2])
            break

    #question = Question.objects.get(id=r)
    result = int(question.result)

    dict = {
        '6 + 8': 14, '6 + 7': 13, '11 + 1': 12, '4 + 7': 11, '10 + 0': 10,
        '6 + 3': 9, '1 + 7': 8, '2 + 5': 7, '3 + 3': 6, '2 + 3': 5,
        '3 + 1': 4, '1 + 2': 3, '1 + 1': 2, '0 + 1': 1, '0 + 0': 0,
    }
    keys = sorted(dict, key=dict.get)
    vals = sorted(dict.values())

    i = randint(0, 100)

    a1 = result + i%4
    a2 = result + (i+1)%4
    a3 = result + (i+2)%4
    a4 = result + (i+3)%4

    template = loader.get_template('i9.html')
    context = {
        'content': question.content,
        'v1': vals[a1],
        'v2': vals[a2],
        'v3': vals[a3],
        'v4': vals[a4],
        'k1': keys[a1],
        'k2': keys[a2],
        'k3': keys[a3],
        'k4': keys[a4],
        'r': str(question.id),
        'tk': keys[result],
        'path': '/static/audio/' + str(r) +'.mp3'
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
