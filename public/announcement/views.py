from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from dongtaoy_oa.views import common_context
from hr.models import Department
from public.models import Message, MessageTo, MessageType


def announcement_publish_index(request):
    groups = Department.objects.all()
    return render(request, 'public/announcement/publish.html', {'groups': groups},
                  context_instance=RequestContext(request, processors=[common_context]))


def announcement_save(request):
    print request.FILES
    return HttpResponse(1)