from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from django.db import transaction
from crm.models import Customer
from crm.models import CustomerType
from django.http import HttpResponse

def customer_index(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer/index.html', {'customers': customers},
                  context_instance=RequestContext(request, processors=[common_context]))


def customer_detail(request):
    types = CustomerType.objects.all()
    try:
        spec_customer = Customer.objects.get(id=request.GET.get('customer_id'))
    except:
        spec_customer = None
    return render(request, 'crm/customer/modal.html', {'spec_customer': spec_customer,
                                                               'types': types})


def customer_save(request):
    customer = Customer(id=request.POST.get('customer_id'),
                  name=request.POST.get('customer_name'),
                  address=request.POST.get('customer_address'),
                  phone=request.POST.get('customer_phone'),
                  email=request.POST.get('customer_email'),
                  fax=request.POST.get('customer_fax'),
                  type=CustomerType.objects.get(id=request.POST.get('customer_type')))
    with transaction.atomic():
        customer.save()
    customers = Customer.objects.all()
    return render(request, 'crm/customer/body.html', {'customers': customers})



def customer_check(request):
    try:
        Customer.objects.get(name=request.POST.get('customer_name'))
        return HttpResponse('{"valid": false}')
    except Exception, e:
        return HttpResponse('{"valid": true}')

def customer_delete(request):
    Customer.objects.get(id=request.POST.get('customer_id')).delete()
    return render_body(request)

def render_body(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer/body.html', {"customers": customers,
                                                 "success": True})