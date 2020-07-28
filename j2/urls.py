from django.conf.urls import url
from j2 import views

app_name = 'j2'

urlpatterns = [
    url(r'^question/$', views.question, name='question'),
    url(r'result/(?P<game>[0-9a-z]+)/$', views.result, name='result'),
]