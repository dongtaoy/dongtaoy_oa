from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.db import transaction
from dongtaoy_oa.views import common_context, permission_tree
from hr.models import Group
from system.models import Permission


def group_permission_index(request):
    groups = Group.objects.all()
    return render(request, 'hr/group/permission/index.html', {"groups": groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def group_permission_detail(request):
    print request
    all_permissions = Permission.objects.all()
    print all_permissions
    group_permissions = Permission.objects.filter(group=Group.objects.get(id=request.GET.get('groupid')))
    print group_permissions
    return render(request, 'hr/group/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group_permissions,
                                                            "groupid": request.GET.get('groupid')})


def group_permission_save(request):
    new_permissions = Permission.objects.filter(id__in=request.POST.getlist('permissions[]'))
    group = Group.objects.get(id=request.POST.get('group_id'))
    with transaction.atomic():
        group.permissions = new_permissions
    all_permissions = Permission.objects.all()
    return render(request, 'hr/group/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group.permissions.all(),
                                                            "groupid": group.id,
                                                            "success": True})