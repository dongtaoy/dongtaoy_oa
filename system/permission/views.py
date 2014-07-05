from django.shortcuts import render, redirect
from django.db import transaction, models
from oa_model.models import OaPermission
from dongtaoy_oa.views import permission_tree
from django_ajax.decorators import ajax
from django.http import HttpResponse


# permission index
def permission_index(request):
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/index.html', {'permissions': permission_tree(all_permissions)})


# permission detail
@ajax
def permission_detail(request):
    spec_permission = OaPermission.objects.get(id=request.GET.get('permission_id'))
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/modal.html', {"spec_permission": spec_permission,
                                                            "permissions": permission_tree(all_permissions)})


# save permission
def permission_mod(request):
    parent = OaPermission.objects.get(id=request.POST.get('permission_parent')) \
        if request.POST.get('permission_parent') != 'NULL' else None
    if not request.POST.get('permission_order'):
        try:
            order = OaPermission.objects.filter(parent=parent).aggregate(models.Max('order'))['order__max'] + 1
        except Exception, e:
            print e
            order = 1
    else:
        order = request.POST.get('permission_order')
    with transaction.atomic():
        OaPermission(id=request.POST.get("permission_id"), url=request.POST.get("permission_url"),
                     name=request.POST.get("permission_name"), parent=parent, order=order).save()
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/index.html', {'permissions': permission_tree(all_permissions),
                                                            'success': 1})
    return redirect("/#system/permission/")


# delete permission
@ajax
def permission_delete(request):
    OaPermission.objects.get(id=request.POST.get("permission_id")).delete()
    all_permissions = OaPermission.objects.all()
    return render(request, 'system/permission/index.html', {'permissions': permission_tree(all_permissions),
                                                            'success': 1})