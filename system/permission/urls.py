from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from system.permission.views import SidebarListView, SidebarCreateView, SidebarUpdateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', SidebarListView.as_view()),


    url(r'^ajax/add/$', permission_required('system.add_sidebar')(SidebarCreateView.as_view())),


    url(r'^ajax/mod/(?P<sidebar>\d+)/$', permission_required('system.change_sidebar')(SidebarUpdateView.as_view())),


    url(r'^ajax/delete/$', 'system.permission.views.permission_delete'),
)
