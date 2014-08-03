from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from django.db import transaction
from system.models import Label
from django.http import HttpResponse

def label_index(request):
    labels = Label.objects.all()
    return render(request, 'system/label/index.html', {'labels': labels},
                  context_instance=RequestContext(request, processors=[common_context]))


def label_detail(request):
    try:
        spec_label = Label.objects.get(id=request.GET.get('label_id'))
    except:
        spec_label = None
    return render(request, 'system/label/modal.html', {'spec_label': spec_label})


def label_save(request):
    Label(id=request.POST.get('label_id'),
                  name=request.POST.get('label_name'),
                  css=request.POST.get('label_css'))
    labels = Label.objects.all()
    return render(request, 'system/label/body.html', {'labels': labels,
                                                                       'success': True})


def label_delete(request):
    Label.objects.get(id=request.POST.get('label_id')).delete()
    labels = Label.objects.all()
    return render(request, 'system/label/body.html', {'labels': labels,
                                                                       'success': True})