from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from hr.models import UserStatus
from hr.status.views import UserStatusCreateView, UserStatusUpdateView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # index
                       url(r'^$', ListView.as_view(
                           model=UserStatus,
                           template_name='hr/status/index.html',
                           context_object_name='userstatuses'
                       )),

                       url(r'^ajax/add/', permission_required('hr.add_userstatus')(UserStatusCreateView.as_view()),
                           name='add_userstatus'),

                       url(r'^ajax/mod/(?P<status>\d+)/',
                           permission_required('hr.change_userstatus')(UserStatusUpdateView.as_view()),
                           name='change_userstatus'),
)
