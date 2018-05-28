from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='user_login'),
    url(r'^logout/$', auth_views.logout, {"template_name": "index.html"}, name='user_logout'),
    url(r'^message/(?P<pk>\d+)/$', views.message_detail, name='message_detail'),
    # url(r'^messageList/$', views.message_list, name='message_list'),
    url(r'^messageList/$', views.message_list, name='message_list'),
    url(r'^messageAdd/$', views.message_add, name='message_add'),
]