from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # group url
    url(r'^$', 'hr.group.views.group_index'),
    url(r'ajax/detail/', 'hr.group.views.group_detail')
)