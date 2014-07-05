from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'dongtaoy_oa.views.index'),
    url(r'^dashboard/', 'dongtaoy_oa.views.dashboard'),
    url(r'^login/$', 'dongtaoy_oa.views.login'),
    url(r'^logout/$', 'dongtaoy_oa.views.logout'),
    url(r'^lock/$', 'dongtaoy_oa.views.lock'),


    url(r'^system/', include('system.urls')),
    url(r'^hr/', include('hr.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
