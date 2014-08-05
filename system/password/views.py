from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context, check_password
from hr.models import Employee
from hashlib import md5


def password_index(request):
    return render(request, 'system/password/index.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def password_mod(request):
    user = Employee.objects.get(id=request.session.get('user_id'))
    user.password = md5(request.POST.get('new_password')+user.salt).hexdigest()
    user.save()
    return render(request, 'system/password/body.html', {'success': True})


def old_password_check(request):
    user = Employee.objects.get(id=request.session.get('user_id'))
    if check_password(user.password, request.POST.get('old_password'), user.salt):
        return HttpResponse('{"valid": true}')
    return HttpResponse('{"valid": false}')