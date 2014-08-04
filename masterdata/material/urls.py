from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),
                       #url(r'^$', 'crm.customer.views.customer_index'),

                       #include
                       url(r'^type/', include('masterdata.material.type.urls')),

                       #views
                       url(r'^$', 'masterdata.material.views.material_index'),
                       url(r'^ajax/detail/', 'masterdata.material.views.material_detail'),
                       url(r'^ajax/save/', 'masterdata.material.views.material_save'),
                       url(r'^ajax/delete/', 'masterdata.material.views.material_delete')
)
