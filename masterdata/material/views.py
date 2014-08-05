from django.template import RequestContext
from django.shortcuts import render
from dongtaoy_oa.views import common_context
from django.db import transaction
from masterdata.models import Material, MaterialType
from hr.models import Group, Employee
import time
from django.http import HttpResponse


def material_index(request):
    materials = Material.objects.all()
    return render(request, 'masterdata/material/index.html', {'materials': materials},
                  context_instance=RequestContext(request, processors=[common_context]))


def material_detail(request):
    types = MaterialType.objects.all()
    groups = Group.objects.all()
    try:
        spec_material = Material.objects.get(id=request.GET.get('material_id'))
    except:
        spec_material = None
    return render(request, 'masterdata/material/modal.html', {'spec_material': spec_material,
                                                              'types': types,
                                                              'groups': groups})


def material_save(request):
    with transaction.atomic():
        if request.POST.get('material_id'):
            material = Material(id=request.POST.get('material_id'),
                                name=request.POST.get('material_name'),
                                description=request.POST.get('material_description'),
                                type=MaterialType.objects.get(id=request.POST.get('material_type')))
            material.save(update_fields=['name', 'description', 'type'])
        else:
            material = Material(name=request.POST.get('material_name'),
                                regtime=time.strftime('%Y-%m-%d'),
                                description=request.POST.get('material_description'),
                                user=Employee.objects.get(id=request.session.get('user_id')),
                                type=MaterialType.objects.get(id=request.POST.get('material_type')))
            material.save()
        material.groups.clear()
        material.groups = Group.objects.filter(id__in=request.POST.getlist('material_groups'))
    return render_body(request)


def material_delete(request):
    Material.objects.get(id=request.POST.get('material_id')).delete()
    return render_body(request)


def render_body(request):
    materials = Material.objects.all()
    return render(request, 'masterdata/material/body.html', {"materials": materials,
                                                             "success": True})