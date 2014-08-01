from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # permission url
    url(r'^permission/', include('system.permission.urls')),
    url(r'^password/', include('system.password.urls'))
)
