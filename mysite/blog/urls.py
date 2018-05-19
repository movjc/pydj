from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    url(r'^detail/(?P<article_id>\d+)/$', views.blog_detail, name="blog_detail"),
]