from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from dongtaoy_oa.views import common_context
from administration.models import AssetCategory, AssetCategoryForm
from system.models import Label


def category_index(request):
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/index.html', {'categories': categories},
                  context_instance=RequestContext(request, processors=[common_context]))


def category_detail(request):
    try:
        spec_category = AssetCategory.objects.get(id=request.GET.get('category_id'))
    except:
        spec_category = None
    form = AssetCategoryForm(instance=spec_category)
    labels = Label.objects.all()
    return render(request, 'administration/asset/category/modal.html', {'form': form,
                                                                        'spec_category': spec_category,
                                                                        'labels': labels})


def category_save(request):
    if request.POST.get('id'):
        category = AssetCategory.objects.get(id=request.POST.get('id'))
    else:
        category = None
    AssetCategoryForm(request.POST, instance=category).save()
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/body.html', {'categories': categories,
                                                                       'success': True})

def category_delete(request):
    AssetCategory.objects.get(id=request.POST.get('category_id')).delete()
    categories = AssetCategory.objects.all()
    return render(request, 'administration/asset/category/body.html', {'categories': categories,
                                                                       'success': True})
