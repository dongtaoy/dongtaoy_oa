from oa_model.models import OaUser, OaGroup, OaUserGroup
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.db import transaction
from dongtaoy_oa.views import common_context
from random import randint
from hashlib import md5


# user index
def user_index(request):
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    return render(request, 'hr/user/index.html', {'users': users,
                                                  'groups': groups},
                  context_instance=RequestContext(request, processors=[common_context]))


# user detail
def user_detail(request):
    try:
        spec_user = OaUser.objects.get(id=request.GET.get('user_id'))
    except Exception, e:
        print e
        spec_user = None
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    user_groups = [x.group for x in OaUserGroup.objects.filter(user=spec_user)]
    return render(request, 'hr/user/modal.html', {'spec_user': spec_user,
                                                  'users': users,
                                                  'groups': groups,
                                                  'user_groups': user_groups})


# save user detail
def user_save(request):
    if request.POST.get('user_id'):
        OaUser.objects.filter(id=request.POST.get('user_id')).update(realname=request.POST.get('user_realname'),
                                                                     sex=request.POST.get('user_sex'),
                                                                     regtime=request.POST.get('user_regtime'),
                                                                     email=request.POST.get('user_email'),
                                                                     phone=request.POST.get('user_phone'),
                                                                     salary=request.POST.get('user_salary'),
                                                                     description=request.POST.get('user_description'),
                                                                     dob=request.POST.get('user_dob'),
                                                                     identifier=request.POST.get('user_identifier'),
                                                                     position=request.POST.get('user_position'),
                                                                     address=request.POST.get('user_address'))
        user = OaUser.objects.get(id=request.POST.get('user_id'))

    else:
        salt = generate_salt()
        OaUser.objects.create(realname=request.POST.get('user_realname'),
                              sex=request.POST.get('user_sex'),
                              regtime=request.POST.get('user_regtime'),
                              email=request.POST.get('user_email'),
                              phone=request.POST.get('user_phone'),
                              salary=request.POST.get('user_salary'),
                              description=request.POST.get('user_description'),
                              dob=request.POST.get('user_dob'),
                              identifier=request.POST.get('user_identifier'),
                              position=request.POST.get('user_position'),
                              address=request.POST.get('user_address'),
                              username=request.POST.get('user_username'),
                              password=md5(request.POST.get('user_password') + salt).hexdigest(),
                              salt=salt)
        user = OaUser.objects.get(username=request.POST.get('user_username'))
    user_groups = request.POST.getlist('user_groups')
    OaUserGroup.objects.filter(user=user).delete()
    with transaction.atomic():
        for user_group in user_groups:
            OaUserGroup(user=user, group=OaGroup.objects.get(id=user_group)).save()
    return render_body(request)


# delete user
def user_delete(request):
    OaUser.objects.get(id=request.POST.get('user_id')).delete()
    return render_body(request)


# check username existence
def user_check(request):
    try:
        OaUser.objects.get(username=request.POST.get('user_username'))
        return HttpResponse('{"valid": false}')
    except Exception, e:
        print e
        return HttpResponse('{"valid": true}')


# render user body
def render_body(request):
    users = OaUser.objects.all()
    return render(request, 'hr/user/body.html', {"users": users,
                                                 "success": True})


# generate salt for user password
def generate_salt():
    return chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122))

