from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # group url
    url(r'^$', 'hr.group.permission.views.group_permission_index'),
    url(r'^ajax/detail/', 'hr.group.permission.views.group_permission_detail'),
    url(r'^ajax/save/', 'hr.group.permission.views.group_permission_save'),
    # url(r'ajax/delete/', 'hr.group.views.group_delete'),

)
