from django.shortcuts import render, redirect
from django.db import transaction, models
from system.models import Permission
from dongtaoy_oa.views import permission_tree, common_context
from django.template import RequestContext
from django.http import HttpResponse


# permission index
def permission_index(request):
    all_permissions = Permission.objects.all()
    return render(request, 'system/permission/index.html', {'success': request.GET.get('success'),
                                                            'permissions': permission_tree(all_permissions)},
                  context_instance=RequestContext(request, processors=[common_context]))


# permission detail
def permission_detail(request):
    try:
        spec_permission = Permission.objects.get(id=request.GET.get('permission_id'))
    except:
        spec_permission = None
    all_permissions = Permission.objects.all()
    return render(request, 'system/permission/modal.html', {"spec_permission": spec_permission,
                                                            "permissions": permission_tree(all_permissions)})


# save permission
def permission_mod(request):
    parent = Permission.objects.get(id=request.POST.get('permission_parent')) \
        if request.POST.get('permission_parent') != 'NULL' else None
    if not request.POST.get('permission_order'):
        try:
            order = Permission.objects.filter(parent=parent).aggregate(models.Max('order'))['order__max'] + 1
        except Exception, e:
            print e
            order = 1
    else:
        order = request.POST.get('permission_order')
    with transaction.atomic():
        Permission(id=request.POST.get("permission_id"), url=request.POST.get("permission_url"),
                     name=request.POST.get("permission_name"), parent=parent, order=order).save()
    all_permissions = Permission.objects.all()
    return render(request, 'system/permission/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})


# delete permission
def permission_delete(request):
    with transaction.atomic():
        Permission.objects.get(id=request.POST.get("permission_id")).delete()
    all_permissions = Permission.objects.all()
    return render(request, 'system/permission/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})