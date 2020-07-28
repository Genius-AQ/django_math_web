from django.conf.urls import url
from j1 import views

app_name = 'j1'

urlpatterns = [
    url(r'^question/$', views.question, name='question'),
    url(r'result/(?P<game>[0-9a-z]+)/$', views.result, name='result'),
]