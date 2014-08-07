from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.db import transaction
from dongtaoy_oa.views import common_context, permission_tree
from hr.models import Department
from system.models import Sidebar


def group_permission_index(request):
    groups = Department.objects.all()
    return render(request, 'hr/department/permission/index.html', {"groups": groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def group_permission_detail(request):
    all_permissions = Sidebar.objects.all()
    group_permissions = Sidebar.objects.filter(group=Department.objects.get(id=request.GET.get('groupid')))
    return render(request, 'hr/department/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group_permissions,
                                                            "groupid": request.GET.get('groupid')})


def group_permission_save(request):
    new_permissions = Sidebar.objects.filter(id__in=request.POST.getlist('permissions[]'))
    group = Department.objects.get(id=request.POST.get('group_id'))
    with transaction.atomic():
        group.permissions = new_permissions
    all_permissions = Sidebar.objects.all()
    return render(request, 'hr/department/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group.permissions.all(),
                                                            "groupid": group.id,
                                                            "success": True})