from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from administration.models import Asset, AssetCategory
from administration.forms import AssetForm
from hr.models import Department
import time


def asset_index(request):
    assets = Asset.objects.all()
    return render(request, 'administration/asset/index.html', {'assets': assets},
                  context_instance=RequestContext(request, processors=[common_context]))


def asset_detail(request):
    try:
        spec_asset = Asset.objects.get(id=request.GET.get('asset_id'))
    except:
        spec_asset = None
    form = AssetForm(instance=spec_asset)
    categories = AssetCategory.objects.all()
    groups = Department.objects.all()
    return render(request, 'administration/asset/modal.html', {'form': form,
                                                               'spec_asset': spec_asset,
                                                               'categories': categories,
                                                               'groups': groups})


def asset_save(request):
    if request.POST.get('asset_id'):
        AssetForm(request.POST, instance=Asset.objects.get(id=request.POST.get('asset_id'))).save()
    else:
        asset = AssetForm(request.POST).save(commit=False)
        asset.regtime = time.strftime('%Y-%m-%d')
        asset.save()
    # with transaction.atomic():
    #     asset.save()
    #     asset.categories.clear()
    #     asset.categories = AssetCategory.objects.filter(id__in=request.POST.getlist('asset_categories'))
    assets = Asset.objects.all()
    return render(request, 'administration/asset/body.html', {'assets': assets})