from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),
                       #url(r'^$', 'crm.customer.views.customer_index'),


                       url(r'^$', 'masterdata.material.type.views.type_index'),
                       url(r'^ajax/detail/', 'masterdata.material.type.views.type_detail'),
                       url(r'^ajax/save/', 'masterdata.material.type.views.type_save'),
                       url(r'^ajax/delete/', 'masterdata.material.type.views.type_delete')
)