from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from system.permission.sidebar.views import SidebarListView, SidebarCreateView, SidebarUpdateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', SidebarListView.as_view()),


                       url(r'^ajax/add/$',
                           permission_required('system.add_sidebar', raise_exception=True)(SidebarCreateView.as_view()),
                           name='add_sidebar'),


                       url(r'^ajax/mod/(?P<sidebar>\d+)/$',
                           permission_required('system.change_sidebar', raise_exception=True)(
                               SidebarUpdateView.as_view()),
                           name='change_sidebar'),


                       url(r'^ajax/delete/$', 'system.permission.sidebar.views.permission_delete'),
)
