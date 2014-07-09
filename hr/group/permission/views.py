from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.db import transaction
from dongtaoy_oa.views import common_context, permission_tree
from oa_model.models import OaGroup, OaPermission, OaGroupPermission


def group_permission_index(request):
    groups = OaGroup.objects.all()
    return render(request, 'hr/group/permission/index.html', {"groups": groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def group_permission_detail(request):
    all_permissions = OaPermission.objects.all()
    group_permissions = [x.permission for x in OaGroupPermission.objects.filter(group=request.GET.get('groupid'))]
    return render(request, 'hr/group/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group_permissions,
                                                            "groupid": request.GET.get('groupid')})


def group_permission_save(request):
    new_permissions = request.POST.getlist('permissions[]')
    group = OaGroup.objects.get(id=request.POST.get('group_id'))
    OaGroupPermission.objects.filter(group=group).delete()
    with transaction.atomic():
        for permission in new_permissions:
            entry = OaGroupPermission(group=group, permission=OaPermission.objects.get(id=permission))
            entry.save()
    all_permissions = OaPermission.objects.all()
    group_permissions = [x.permission for x in OaGroupPermission.objects.filter(group=group)]
    return render(request, 'hr/group/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                            "group_permissions": group_permissions,
                                                            "groupid": group.id,
                                                            "success": True})
    return HttpResponse(1);