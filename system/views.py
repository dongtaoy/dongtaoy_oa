from django.shortcuts import render
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

@ajax
def permission_save(request):
    permissions = loads(request.POST.get('permissions'))
    print permissions
    return 1