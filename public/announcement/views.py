from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context


def announcement_publish(request):
    return  render(request, 'public/announcement/publish.html', {},
                   context_instance=RequestContext(request, processors=[common_context]))