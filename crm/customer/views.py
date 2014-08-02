from django.shortcuts import render, redirect
from hr.models import User
from system.models import Permission
from django.template import RequestContext
from collections import defaultdict
from hashlib import md5

def customer_check(request):
    try:
        User.objects.get(username=request.POST.get('user_username'))
        return HttpResponse('{"valid": false}')
    except Exception, e:
        return HttpResponse('{"valid": true}')