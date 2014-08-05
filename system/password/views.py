from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context


def password_index(request):
    return render(request, 'system/password/index.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))


def password_mod(request):
    request.user.set_password(request.POST.get('new_password'))
    return render(request, 'system/password/body.html', {'success': True})


def old_password_check(request):
    if request.user.check_password(request.POST.get('old_password')):
        return HttpResponse('{"valid": true}')
    return HttpResponse('{"valid": false}')