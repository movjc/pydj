"""enterpriseDailySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from dailySystem import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^message/(?P<pk>\d+)/$', views.message_detail, name='message_detail'),
    url(r'^messageList/$', views.message_list, name='message_list'),
    url(r'^messageAdd/$', views.message_add, name='message_add'),
    url(r'^messagePost/$', views.message_posts, name='message_posts'),
    url(r'^messagePage/$', views.pag_post, name='pag_post'),
    url(r'^paginPage/$', views.pagin_post, name='pagin_post'),
]
