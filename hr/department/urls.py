from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from hr.models import Department
from hr.department.views import DepartmentCreateView, DepartmentUpdateView


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # group url
    url(r'^$',
        (ListView.as_view(
            model=Department,
            context_object_name='groups',
            template_name='hr/department/index.html'))),


    url(r'^ajax/add/',
        permission_required('hr.add_department', raise_exception=True)(DepartmentCreateView.as_view()),
        name='department_create'),


    url(r'^ajax/mod/(?P<department>\d+)/$',
        permission_required('hr.change_department', raise_exception=True)(DepartmentUpdateView.as_view()),
        name='department_mod'),


    url(r'^ajax/delete/', 'hr.department.views.group_delete'),


    url(r'^ajax/check/', 'hr.department.views.group_check'),


    url(r'^permission/', include('hr.department.permission.urls'))
)
