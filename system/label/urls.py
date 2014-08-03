from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    url(r'^$', 'system.label.views.label_index'),
    url(r'^ajax/save/', 'system.label.views.label_save'),
    url(r'^ajax/detail/', 'system.label.views.label_detail'),
    url(r'^ajax/delete/', 'system.label.views.label_delete'),
)
