# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from random import randint
from models import Picture
import os, csv
from django.template import loader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def question(request):

    # q = Picture.objects.get(id=randint(0, 14))
    r = randint(0, 14)
    while (r == StaticVar.last):
        r = randint(0,14)
    StaticVar.last = r

    dataReader = csv.reader(open(os.path.join(BASE_DIR, 'pic.csv')), delimiter=',', quotechar='"')
    for row in dataReader:
        if int(row[0]) == r:
            q = Picture(id=row[0], name=row[1], sum=row[2], result=row[3])
            break

    path = '/static/pic/' + q.name + '.png'

    template = loader.get_template('j1.html')
    context = {
        'path': path,
        'n1': int(q.sum),
        'n2': int(q.sum) - int(q.result),
        'result': int(q.result)
    }

    return HttpResponse(template.render(context, request))

def result(request, game):

    if request.method=="POST":
        result = request.POST.get('result')
        number = request.POST.get('number')
        print number

        t = [u'CHÍNH XÁC!', u'QUÁ CHUẨN!', u'RẤT TỐT = ))', u'TUYỆT VỜI ^^', u'CHUẨN LUÔN ; )']
        f = [u'Sai roài :(', u'Không đúng T.T', u'Tính lại đi!']

        if int(result)==int(number):
            template = loader.get_template('correct.html')
            context = {
                'game': game+':question',
                'sentence': t[randint(0,4)]
            }

        else:
            template = loader.get_template('incorrect.html')
            context = {
                'game': game+':question',
                'key': result,
                'sentence': f[randint(0, 2)]
            }

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseBadRequest()

class StaticVar:
    last = 0