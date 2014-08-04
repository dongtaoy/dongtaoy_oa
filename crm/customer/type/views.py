from crm.models import CustomerType
from system.models import Label
from django.shortcuts import render
from django.template import RequestContext
from django.db import transaction
from dongtaoy_oa.views import common_context


def type_index(request):
    types = CustomerType.objects.all()
    return render(request, 'crm/customer/type/index.html', {'types': types},
                  context_instance=RequestContext(request, processors=[common_context]))


def type_detail(request):
    labels = Label.objects.all()
    try:
        spec_type = CustomerType.objects.get(id=request.GET.get('type_id'))
    except:
        spec_type = None
    return render(request, 'crm/customer/type/modal.html', {'spec_type': spec_type,
                                                            'labels': labels})


def type_save(request):
    print request.POST
    with transaction.atomic():
        CustomerType(id=request.POST.get('type_id'),
                     name=request.POST.get('type_name'),
                     description=request.POST.get('type_description'),
                     label=Label.objects.get(id=request.POST.get('type_label'))).save()
    types = CustomerType.objects.all()
    return render(request, 'crm/customer/type/body.html', {'types': types,
                                                           'success': True})


def type_delete(request):
    CustomerType.objects.get(id=request.POST.get('type_id')).delete()
    types = CustomerType.objects.all()
    return render(request, 'crm/customer/type/body.html', {'types': types,
                                                           'success': True})