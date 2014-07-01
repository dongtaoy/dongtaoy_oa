from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'oa.views.index'),
    url(r'^dashboard/', 'oa.views.dashboard'),
    url(r'^login/', 'oa.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)
