from django.shortcuts import render
from django.template import RequestContext
from django.db import transaction
from hr.models import Group, Employee
from system.models import Label
from dongtaoy_oa.views import common_context


def group_index(request):
    groups = Group.objects.all()
    return render(request, 'hr/group/index.html', {"groups": groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def group_detail(request):
    users = Employee.objects.all()
    labels = Label.objects.all()
    try:
        spec_group = Group.objects.get(id=request.GET.get('group_id'))
    except Exception:
        spec_group = None
    return render(request, 'hr/group/modal.html', {"spec_group": spec_group,
                                                   "users": users,
                                                   "labels": labels})


def group_mod(request):
    with transaction.atomic():
        Group(id=request.POST.get('group_id'),
              name=request.POST.get('group_name'),
              leader=Employee.objects.get(id=request.POST.get('group_leader')),
              description=request.POST.get('group_description'),
              label=Label.objects.get(id=request.POST.get('group_label'))).save()
    groups = Group.objects.all()
    return render(request, 'hr/group/body.html', {"success": True,
                                                  "groups": groups})


def group_delete(request):
    Group.objects.get(id=request.POST.get('group_id')).delete()
    groups = Group.objects.all()
    return render(request, 'hr/group/body.html', {"success": True,
                                                  "groups": groups})