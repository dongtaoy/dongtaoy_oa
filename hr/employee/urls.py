from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.models import User
from hr.employee.views import EmployeeCreateView, EmployeeUpdateView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # user url
    url(r'^$', ListView.as_view(
        model=User,
        queryset=User.objects.filter(is_active=1),
        context_object_name='users',
        template_name='hr/employee/index.html')),


    url(r'^ajax/add/', EmployeeCreateView.as_view()),

    url(r'^ajax/mod/(?P<employee>\d+)/', EmployeeUpdateView.as_view()),

    # url(r'ajax/detail/', 'hr.employee.views.user_detail'),
    url(r'ajax/delete/', 'hr.employee.views.user_delete'),
    url(r'ajax/check/', 'hr.employee.views.user_check'),
)
