from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context
from hr.models import Userstatus


def userstatus_index(request):
    userstatuses = Userstatus.objects.all()
    return render(request, 'hr/status/index.html', {'userstatuses': userstatuses},
                  context_instance=RequestContext(request, processors=[common_context]))


def userstatus_detail(request):
    try:
        spec_userstatus = Userstatus.objects.get(id=request.GET.get('userstatus_id'))
    except Exception, e:
        spec_userstatus = None
    return render(request, 'hr/status/modal.html', {'spec_userstatus': spec_userstatus})


def userstatus_save(request):
    Userstatus(id=request.POST.get('userstatus_id'),
                 name=request.POST.get('userstatus_name'),
                 description=request.POST.get('userstatus_description'),
                 label=request.POST.get('userstatus_label')).save()
    userstatuses = Userstatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})


def userstatus_delete(request):
    Userstatus.objects.get(id=request.POST.get('userstatus_id')).delete()
    userstatuses = Userstatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})