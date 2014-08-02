from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    #index
    url(r'^$', 'crm.customer.type.views.type_index'),

    # detail
    url(r'^ajax/detail/', 'crm.customer.type.views.type_detail'),

    # save
    url(r'^ajax/save/', 'crm.customer.type.views.type_save'),

    # delete
    url(r'^ajax/delete/', 'crm.customer.type.views.type_delete')
)
