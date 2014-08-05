from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from django.db import transaction
from system.models import Label
from masterdata.models import Material,MaterialType
from hr.models import Department
from django.http import HttpResponse


def type_index(request):
    types = MaterialType.objects.all()
    return render(request, 'masterdata/material/type/index.html', {'types': types},
                  context_instance=RequestContext(request, processors=[common_context]))


def type_detail(request):
    labels = Label.objects.all()
    try:
        spec_type = MaterialType.objects.get(id=request.GET.get('type_id'))
    except:
        spec_type = None
    return render(request, 'masterdata/material/type/modal.html', {'spec_type': spec_type,
                                                            'labels': labels})


def type_save(request):
    print request.POST
    with transaction.atomic():
        MaterialType(id=request.POST.get('type_id'),
                     name=request.POST.get('type_name'),
                     description=request.POST.get('type_description'),
                     label=Label.objects.get(id=request.POST.get('type_label'))).save()
    types = MaterialType.objects.all()
    return render(request, 'masterdata/material/type/body.html', {'types': types,
                                                           'success': True})


def type_delete(request):
    MaterialType.objects.get(id=request.POST.get('type_id')).delete()
    types = MaterialType.objects.all()
    return render(request, 'masterdata/material/type/body.html', {'types': types,
                                                           'success': True})