from django.shortcuts import render
from django.db import transaction
from oa_model.models import OaGroup, OaGroupPermission, OaPermission
from dongtaoy_oa.views import permission_tree
from django_ajax.decorators import ajax
from json import loads

from django.http import HttpResponse


# permission landing page
def permission_index(request):
    groups = OaGroup.objects.all()
    return render(request, 'system/permission/index.html', {'groups': groups})


# AJAX get permission
@ajax
def permission_detail(request):
    all_permissions = OaPermission.objects.all()
    group_permissions = [x.permission for x in OaGroupPermission.objects.filter(group=request.GET.get('groupid'))]
    return render(request, 'system/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                          "group_permissions": group_permissions,
                                                          "groupid": request.GET.get('groupid')})


# AJAX save permission
@ajax
def permission_save(request):
    new_permissions = loads(request.POST.get('permissions'))
    print new_permissions
    group = OaGroup.objects.get(id=request.POST.get('groupid'))
    OaGroupPermission.objects.filter(group=group).delete()
    with transaction.atomic():
        for permission in new_permissions:
            entry = OaGroupPermission(group=group, permission=OaPermission.objects.get(id=permission))
            entry.save()
    all_permissions = OaPermission.objects.all()
    group_permissions = [x.permission for x in OaGroupPermission.objects.filter(group=group)]
    return render(request, 'system/permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                          "group_permissions": group_permissions,
                                                          "groupid": group.id})