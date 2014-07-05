from django.shortcuts import render, redirect
from django.db import transaction, models
from oa_model.models import OaGroup, OaGroupPermission, OaPermission, OaUser, OaUserGroup
from dongtaoy_oa.views import permission_tree
from django_ajax.decorators import ajax
from json import loads
from django.http import HttpResponse


# group_permission landing page
def group_permission_index(request):
    groups = OaGroup.objects.all()
    return render(request, 'system/group_permission/index.html', {'groups': groups})


# AJAX get group_permission
@ajax
def group_permission_detail(request):
    all_permissions = OaPermission.objects.all()
    group_permissions = [x.permission for x in OaGroupPermission.objects.filter(group=request.GET.get('groupid'))]
    return render(request, 'system/group_permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                                "group_permissions": group_permissions,
                                                                "groupid": request.GET.get('groupid')})


# AJAX save group_permission
@ajax
def group_permission_save(request):
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
    return render(request, 'system/group_permission/mod.html', {"all_permissions": permission_tree(all_permissions),
                                                                "group_permissions": group_permissions,
                                                                "groupid": group.id})


# user_group landing page
def user_group_index(request):
    users = OaUser.objects.all()
    return render(request, 'system/user_group/index.html', {'users': users})


# AJAX detail group info
@ajax
def user_group_detail(request):
    all_groups = OaGroup.objects.all()
    user = OaUser.objects.get(id=request.GET.get('userid'))
    user_groups = [x.group for x in OaUserGroup.objects.filter(user=user)]
    print all_groups
    print user_groups
    return render(request, 'system/user_group/mod.html', {"all_groups": all_groups,
                                                          "user_groups": user_groups,
                                                          "userid": user.id})


# AJAX save user_group info
@ajax
def user_group_save(request):
    new_groups = loads(request.POST.get('groups'))
    print new_groups
    user = OaUser.objects.get(id=request.POST.get('userid'))
    print request.POST.get('userid')
    print user
    OaUserGroup.objects.filter(user=user).delete()
    with transaction.atomic():
        for group in new_groups:
            entry = OaUserGroup(user=user, group=OaGroup.objects.get(id=group))
            entry.save()
    all_groups = OaGroup.objects.all()
    user_groups = [x.group for x in OaUserGroup.objects.filter(user=user)]
    return render(request, 'system/user_group/mod.html', {"all_groups": all_groups,
                                                          "user_groups": user_groups,
                                                          "userid": user.id})


def permission_order_index(request):
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/order.html', {'permissions': permission_tree(all_permissions)})


@ajax
def permission_order_save(request):
    order_maps = loads(request.POST.get('order_maps'))
    for order_map in order_maps:
        OaPermission.objects.filter(id=order_map[0]).update(order=order_map[1])
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/order.html', {'permissions': permission_tree(all_permissions)})


