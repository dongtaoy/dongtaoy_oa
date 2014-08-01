from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # index
    url(r'^$', 'hr.status.views.userstatus_index'),
    url(r'^ajax/detail/', 'hr.status.views.userstatus_detail'),
    url(r'^ajax/save/', 'hr.status.views.userstatus_save'),
    url(r'^ajax/delete/', 'hr.status.views.userstatus_delete')
)
