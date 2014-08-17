from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sidebar/', include('system.permission.sidebar.urls')),
    url(r'^employee/', RedirectView.as_view(
        url='/admin/auth/user/'
    )),
    url(r'^department/', RedirectView.as_view(
        url='/admin/auth/group/'
    ))
)
