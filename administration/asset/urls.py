from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # index
    url(r'^$', 'administration.asset.views.asset_index'),


    # category
    url(r'^category/', include('administration.asset.category.urls'))
)
