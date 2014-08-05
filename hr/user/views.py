from hr.models import Employee, Group, Userstatus
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.db import transaction
from dongtaoy_oa.views import common_context
from random import randint
from hashlib import md5


# user index
def user_index(request):
    users = Employee.objects.all()
    groups = Group.objects.all()
    return render(request, 'hr/user/index.html', {'users': users,
                                                  'groups': groups},
                  context_instance=RequestContext(request, processors=[common_context]))


# user detail
def user_detail(request):
    try:
        spec_user = Employee.objects.get(id=request.GET.get('user_id'))
        user_group = spec_user.groups.all()
    except Exception, e:
        spec_user = None
        user_group = None
    users = Employee.objects.all()
    groups = Group.objects.all()
    user_statuses = Userstatus.objects.all()
    return render(request, 'hr/user/modal.html', {'spec_user': spec_user,
                                                  'users': users,
                                                  'groups': groups,
                                                  'userstatuses': user_statuses,
                                                  'user_groups': user_group})


# save user detail
def user_save(request):
    if request.POST.get('user_id'):
        Employee.objects.filter(id=request.POST.get('user_id')).update(realname=request.POST.get('user_realname'),
                                                                   sex=request.POST.get('user_sex'),
                                                                   regtime=request.POST.get('user_regtime').replace('_',
                                                                                                                    ''),
                                                                   email=request.POST.get('user_email'),
                                                                   phone=request.POST.get('user_phone'),
                                                                   salary=request.POST.get('user_salary'),
                                                                   description=request.POST.get('user_description'),
                                                                   dob=request.POST.get('user_dob').replace('_', ''),
                                                                   identifier=request.POST.get('user_identifier'),
                                                                   position=request.POST.get('user_position'),
                                                                   address=request.POST.get('user_address'),
                                                                   status=Userstatus.objects.get(
                                                                       id=request.POST.get('user_status')))
        user = Employee.objects.get(id=request.POST.get('user_id'))
    else:
        salt = generate_salt()
        Employee.objects.create(realname=request.POST.get('user_realname'),
                            sex=request.POST.get('user_sex'),
                            regtime=request.POST.get('user_regtime').replace('_', ''),
                            email=request.POST.get('user_email'),
                            phone=request.POST.get('user_phone'),
                            salary=request.POST.get('user_salary'),
                            description=request.POST.get('user_description'),
                            dob=request.POST.get('user_dob').replace('_', ''),
                            identifier=request.POST.get('user_identifier'),
                            position=request.POST.get('user_position'),
                            address=request.POST.get('user_address'),
                            status=Userstatus.objects.get(id=request.POST.get('user_status')),
                            username=request.POST.get('user_username'),
                            password=md5(request.POST.get('user_password') + salt).hexdigest(),
                            salt=salt)
        user = Employee.objects.get(username=request.POST.get('user_username'))
    user_groups = Group.objects.filter(id__in=request.POST.getlist('user_groups'))
    with transaction.atomic():
        user.groups = user_groups
    return render_body(request)


# delete user
def user_delete(request):
    Employee.objects.get(id=request.POST.get('user_id')).delete()
    return render_body(request)


# check username existence
def user_check(request):
    try:
        Employee.objects.get(username=request.POST.get('user_username'))
        return HttpResponse('{"valid": false}')
    except Exception, e:
        return HttpResponse('{"valid": true}')


# render user body
def render_body(request):
    users = Employee.objects.all()
    return render(request, 'hr/user/body.html', {"users": users,
                                                 "success": True})


# generate salt for user password
def generate_salt():
    return chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122))

