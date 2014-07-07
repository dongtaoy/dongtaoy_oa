from oa_model.models import OaUser, OaGroup, OaUserGroup
from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from hashlib import md5

# user index
def user_index(request, success=0):
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    return render(request, 'hr/user/index.html', {'users': users,
                                                  'groups': groups,
                                                  'success': success})


# user detail
def user_detail(request):
    spec_user = OaUser.objects.get(id=request.GET.get('user_id'))
    users = OaUser.objects.all()
    groups = OaGroup.objects.all()
    user_groups = [x.group for x in OaUserGroup.objects.filter(user=spec_user)]
    return render(request, 'hr/user/modal.html', {'spec_user': spec_user,
                                                  'users': users,
                                                  'groups': groups,
                                                  'user_groups': user_groups})


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
    for user_group in user_groups:
        OaUserGroup(user=user, group=OaGroup.objects.get(id=user_group)).save()
    return user_index(request, 1)


def user_delete(request):
    OaUser.objects.get(id=request.POST.get('user_id')).delete()
    return user_index(request, 1)


def generate_salt():
    return chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122)) + chr(randint(65, 122))