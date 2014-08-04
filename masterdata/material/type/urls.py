from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),
                       #url(r'^$', 'crm.customer.views.customer_index'),

                       #include
                       url(r'^type/', include('crm.customer.type.urls')),

                       #views
                       url(r'^$', 'crm.customer.views.customer_index'),
                       url(r'^ajax/detail/', 'crm.customer.views.customer_detail'),
                       url(r'^ajax/save/', 'crm.customer.views.customer_save'),
                       url(r'^ajax/delete/', 'crm.customer.views.customer_delete')
)
