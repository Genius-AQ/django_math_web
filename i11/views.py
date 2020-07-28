# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from random import randint
import os
from django.template import loader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def question(request):

    h = randint(0, 100)
    s = randint(h, 100)

    template = loader.get_template('i11.html')
    context = {
        'result': s-h,
        'h': h,
        's': s,
        'position': randint(1,2)
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
