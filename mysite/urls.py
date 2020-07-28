"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,  url
from django.contrib import admin
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i9/', include('i9.urls', namespace='i9')),
    url(r'^i10/', include('i10.urls', namespace='i10')),
    url(r'^i11/', include('i11.urls', namespace='i11')),
    url(r'^j1/', include('j1.urls', namespace='j1')),
    url(r'^j2/', include('j2.urls', namespace='j2')),
    url(r'^$', RedirectView.as_view(url = reverse_lazy('i9:index')))
]
