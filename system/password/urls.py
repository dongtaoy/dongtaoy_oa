from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'system.password.views.password_index'),
    url(r'^ajax/check/$', 'system.password.views.old_password_check'),
    url(r'^ajax/save/$', 'system.password.views.password_mod')
)
