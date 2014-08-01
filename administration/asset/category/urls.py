from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # index
    url(r'^$', 'administration.asset.category.views.category_index'),

    # detail
    url(r'^ajax/detail/', 'administration.asset.category.views.category_detail'),

    # save
    url(r'^ajax/save/', 'administration.asset.category.views.category_save')


)
