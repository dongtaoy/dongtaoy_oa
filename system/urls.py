from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^permission/$', 'system.views.permission_index'),
    url(r'^permission/ajax/detail/', 'system.views.permission_detail'),
    url(r'^permission/ajax/save/', 'system.views.permission_save')
)
