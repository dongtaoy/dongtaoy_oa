from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # user url
    url(r'^$', 'hr.user.views.user_index'),
    url(r'ajax/save/', 'hr.user.views.user_save'),
    url(r'ajax/detail/', 'hr.user.views.user_detail'),
    url(r'ajax/delete/', 'hr.user.views.user_delete'),
    url(r'ajax/check/', 'hr.user.views.user_check'),
)
