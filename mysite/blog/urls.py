from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),##titles/
    url(r'^detail/(?P<article_id>\d+)/$', views.blog_detail, name="blog_detail"),
]
