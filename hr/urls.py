from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # user url
                       url(r'^user/', include('hr.user.urls')),

                       # group url
                       url(r'^group/', include('hr.group.urls')),

                       # status url
                       url(r'^status/', include('hr.status.urls'))
)
