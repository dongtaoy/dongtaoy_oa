from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context
from hr.models import UserStatus
from system.models import Label


def userstatus_index(request):
    userstatuses = UserStatus.objects.all()
    return render(request, 'hr/status/index.html', {'userstatuses': userstatuses},
                  context_instance=RequestContext(request, processors=[common_context]))


def userstatus_detail(request):
    labels = Label.objects.all()
    try:
        spec_userstatus = UserStatus.objects.get(id=request.GET.get('userstatus_id'))
    except Exception, e:
        spec_userstatus = None
    return render(request, 'hr/status/modal.html', {'spec_userstatus': spec_userstatus,
                                                    'labels': labels})


def userstatus_save(request):
    UserStatus(id=request.POST.get('userstatus_id'),
               name=request.POST.get('userstatus_name'),
               description=request.POST.get('userstatus_description'),
               label=Label.objects.get(id=request.POST.get('userstatus_label'))).save()
    userstatuses = UserStatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})


def userstatus_delete(request):
    UserStatus.objects.get(id=request.POST.get('userstatus_id')).delete()
    userstatuses = UserStatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})