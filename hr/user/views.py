from hr.models import Employee
from hr.forms import EmployeeForm
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from dongtaoy_oa.views import common_context


# user index
def user_index(request):
    return render(request, 'hr/user/index.html', {'users': [x for x in Employee.objects.all() if x.user.is_superuser]},
                  context_instance=RequestContext(request, processors=[common_context]))


# user detail
def user_detail(request):
    try:
        spec_user = Employee.objects.get(id=request.GET.get('user_id'))
    except Exception:
        spec_user = None
    form = EmployeeForm(instance=spec_user)
    groups = Group.objects.all()
    return render(request, 'hr/user/modal.html', {'spec_user': spec_user,
                                                  'groups': groups,
                                                  'form': form})


# save user detail
def user_save(request):
    if request.POST.get('user_id'):
        employee = Employee.objects.get(id=request.POST.get('user_id'))
        employee.user.groups = Group.objects.filter(id__in=request.POST.get('user_groups'))
        employee.user.save()
        EmployeeForm(request.POST, instance=employee).save()
    else:
        user = User.objects.create_user(request.POST.get('user_username'), request.POST.get('user_password'))
        user.groups = Group.objects.filter(id__in=request.POST.get('user_groups'))
        employee = EmployeeForm(request.POST).save(commit=False)
        employee.user = user
        employee.save()
    return render(request, 'hr/user/body.html', {"users": [x for x in Employee.objects.all() if x.user.is_superuser],
                                                 "success": True})


# delete user
def user_delete(request):
    user = Employee.objects.get(id=request.POST.get('user_id')).user
    user.is_active = 0
    user.save()
    return render(request, 'hr/user/body.html', {"users": [x for x in Employee.objects.all() if x.user.is_superuser],
                                                 "success": True})


# check username existence
def user_check(request):
    try:
        User.objects.get(username=request.POST.get('user_username'))
        return HttpResponse('{"valid": false}')
    except:
        return HttpResponse('{"valid": true}')

