from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', views.column_detail, name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', views.article_detail, name='article'),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)