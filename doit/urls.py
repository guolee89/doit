# coding: utf-8

from django.conf.urls import patterns, include, url
from views import IndexView, ArticleDetailView
# admin
from django.contrib import admin
admin.autodiscover()

# xadmin
import xadmin
xadmin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'doit.views.home', name='home'),
    url(r'^index/', IndexView.as_view(), name='index_view'),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article_detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
)
