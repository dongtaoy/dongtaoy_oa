from django.shortcuts import render
from django.db import transaction
from system.models import Sidebar
from system.forms import SidebarForm
from dongtaoy_oa.views import permission_tree, common_context
from django.template import RequestContext


# permission index
def permission_index(request):
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/index.html', {'success': request.GET.get('success'),
                                                            'permissions': permission_tree(all_permissions)},
                  context_instance=RequestContext(request, processors=[common_context]))


# permission detail
def permission_detail(request):
    try:
        spec_permission = Sidebar.objects.get(id=request.GET.get('permission_id'))
    except:
        spec_permission = None
    form = SidebarForm(instance=spec_permission)
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/modal.html', {"spec_permission": spec_permission,
                                                            "permissions": permission_tree(all_permissions),
                                                            "form": form})


# save permission
def permission_mod(request):
    # parent = Sidebar.objects.get(id=request.POST.get('permission_parent')) \
    #     if request.POST.get('permission_parent') != 'NULL' else None
    # if not request.POST.get('permission_order'):
    #     try:
    #         order = Sidebar.objects.filter(parent=parent).aggregate(models.Max('order'))['order__max'] + 1
    #     except Exception, e:
    #         print e
    #         order = 1
    # else:
    #     order = request.POST.get('permission_order')

    if request.POST.get("permission_id"):
        SidebarForm(request.POST, instance=Sidebar.objects.get(id=request.POST.get("permission_id"))).save()
    else:
        SidebarForm(request.POST).save()
    # with transaction.atomic():
    #     Sidebar(id=request.POST.get("permission_id"), url=request.POST.get("permission_url"),
    #                  name=request.POST.get("permission_name"), parent=parent, order=order).save()
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})


# delete permission
def permission_delete(request):
    with transaction.atomic():
        Sidebar.objects.get(id=request.POST.get("permission_id")).delete()
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})