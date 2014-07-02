from django.shortcuts import render
from oa_model.models import OaUser
from django.http import HttpResponse


def permission(request):
    users = OaUser.objects.all()
    return render(request, 'system/permission/list.html', {'employees': users})

