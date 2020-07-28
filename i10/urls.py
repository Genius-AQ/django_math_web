from django.conf.urls import url
from i10 import views

app_name = 'i10'

urlpatterns = [
    url(r'^question/$', views.question, name='question'),
    url(r'result/(?P<game>[0-9a-z]+)/$', views.result, name='result'),
]