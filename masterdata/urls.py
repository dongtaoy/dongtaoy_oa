from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','dongtaoy_oa.crm.views.customer_index'),
    url(r'^material/', include('masterdata.material.urls')),

)
