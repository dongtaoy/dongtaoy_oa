from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^group_permission/$', 'system.views.group_permission_index'),
    url(r'^group_permission/ajax/detail/', 'system.views.group_permission_detail'),
    url(r'^group_permission/ajax/save/', 'system.views.group_permission_save'),

    url(r'user_group/$', 'system.views.user_group_index'),
    url(r'user_group/ajax/detail/', 'system.views.user_group_detail'),
    url(r'user_group/ajax/save/', 'system.views.user_group_save'),

    url(r'permission/$', 'system.views.permission_index'),
    url(r'permission/ajax/mod/$', 'system.views.permission_mod'),
    url(r'permission/ajax/detail/', 'system.views.permission_detail'),
    url(r'permission/ajax/delete/', 'system.views.permission_delete'),

    url(r'permission/order/$', 'system.views.permission_order_index'),
    url(r'permission/order/ajax/save/$', 'system.views.permission_order_save')
)
