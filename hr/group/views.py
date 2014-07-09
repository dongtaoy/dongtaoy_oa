from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from oa_model.models import OaGroup, OaUser

from dongtaoy_oa.views import common_context


def group_index(request):
    groups = OaGroup.objects.all()
    return render(request, 'hr/group/index.html', {"groups": groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def group_detail(request):
    users = OaUser.objects.all()
    try:
        spec_group = OaGroup.objects.get(id=request.GET.get('group_id'))
    except Exception, e:
        print e
        spec_group = None
    return render(request, 'hr/group/modal.html', {"spec_group": spec_group,
                                                   "users": users})


def group_mod(request):
    print request.POST
    OaGroup(id=request.POST.get('group_id'),
            name=request.POST.get('group_name'),
            leader=OaUser.objects.get(id=request.POST.get('group_leader')),
            description=request.POST.get('group_description')).save()
    groups = OaGroup.objects.all()
    return render(request, 'hr/group/body.html', {"success": True,
                                                  "groups": groups})


def group_delete(request):
    OaGroup.objects.get(id=request.POST.get('group_id')).delete()
    groups = OaGroup.objects.all()
    return render(request, 'hr/group/body.html', {"success": True,
                                                  "groups": groups})