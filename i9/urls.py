from django.conf.urls import url
from i9 import views

app_name = 'i9'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'content/$', views.content, name='content'),
    url(r'question/$', views.question, name='question'),
    url(r'result/(?P<game>[0-9a-z]+)/$', views.result, name='result'),
]