from django.conf.urls import patterns, include, url

# admin
from django.contrib import admin
admin.autodiscover()

# xadmin
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'doit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/', include(xadmin.site.urls)),
)
