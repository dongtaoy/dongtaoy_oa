from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context
from administration.models import AssetCategory


def category_index(request):
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/index.html', {'categories': categories},
                  context_instance=RequestContext(request, processors=[common_context]))


def category_detail(request):
    try:
        spec_category = AssetCategory.objects.get(id=request.GET.get('category_id'))
    except:
        spec_category = None
    return render(request, 'administration/asset/category/modal.html', {'category': spec_category})


def category_save(request):
    print request.POST
    AssetCategory(id=request.POST.get('category_id'),
                  name=request.POST.get('category_name'),
                  description=request.POST.get('category_description')).save()
    return HttpResponse(1)