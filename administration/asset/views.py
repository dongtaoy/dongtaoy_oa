from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from django.db import transaction
from administration.models import Asset, AssetCategory
from hr.models import Group
import time


def asset_index(request):
    assets = Asset.objects.all()
    return render(request, 'administration/asset/index.html', {'assets': assets},
                  context_instance=RequestContext(request, processors=[common_context]))


def asset_detail(request):
    categories = AssetCategory.objects.all()
    groups = Group.objects.all()
    try:
        spec_asset = Asset.objects.get(id=request.GET.get('asset_id'))
    except:
        spec_asset = None
    return render(request, 'administration/asset/modal.html', {'spec_asset': spec_asset,
                                                               'categories': categories,
                                                               'groups': groups})


def asset_save(request):
    print request.POST
    asset = Asset(id=request.POST.get('asset_id'),
                  brand=request.POST.get('asset_brand'),
                  model=request.POST.get('asset_model'),
                  group=Group.objects.get(id=request.POST.get('asset_group')),
                  usage=int(request.POST.get('asset_usage')),
                  regtime=time.strftime("%Y-%m-%d"),
                  description=request.POST.get('asset_description'))
    with transaction.atomic():
        asset.save()
        asset.categories.clear()
        asset.categories = AssetCategory.objects.filter(id__in=request.POST.getlist('asset_categories'))
    assets = Asset.objects.all()
    return render(request, 'administration/asset/body.html', {'assets': assets})