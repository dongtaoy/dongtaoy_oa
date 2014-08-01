from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'system.permission.views.permission_index'),
    url(r'^save/$', 'system.permission.views.permission_mod'),
    url(r'^ajax/detail/', 'system.permission.views.permission_detail'),
    url(r'^ajax/delete/$', 'system.permission.views.permission_delete'),
)
