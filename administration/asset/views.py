from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context


def asset_index(request):
    return render(request, 'administration/asset/index.html', {},
                  context_instance=RequestContext(request, processors=[common_context]))

