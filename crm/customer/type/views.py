from django.shortcuts import render, redirect
from crm.models import CustomerType
from system.models import Permission
from django.template import RequestContext
from collections import defaultdict
from hashlib import md5


def type_index(request):
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/index.html', {'categories': categories},
                  context_instance=RequestContext(request, processors=[common_context]))


def type_detail(request):
    try:
        spec_category = AssetCategory.objects.get(id=request.GET.get('category_id'))
    except:
        spec_category = None
    return render(request, 'administration/asset/category/modal.html', {'spec_category': spec_category})


def type_save(request):
    print request.POST
    AssetCategory(id=request.POST.get('category_id'),
                  name=request.POST.get('category_name'),
                  description=request.POST.get('category_description'),
                  label=request.POST.get('category_label')).save()
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/body.html', {'categories': categories,
                                                                       'success': True})


def type_delete(request):
    AssetCategory.objects.get(id=request.POST.get('category_id')).delete()
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/body.html', {'categories': categories,
                                                                       'success': True})