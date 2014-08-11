# encoding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from masterdata.models import Material
from masterdata.forms import MaterialForm


class MaterialCreateView(CreateView):
    form_class = MaterialForm
    template_name = 'masterdata/material/modal.html'
    success_url = '/masterdata/material/'

    def get_context_data(self, **kwargs):
        context = super(MaterialCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_material')
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            #user = User.objects.create_user(self.request.POST.get('username'))

            material.groups = Group.objects.filter(id__in=self.request.POST.getlist('groups'))
            material.name = self.request.POST.get('name')
            material.description = self.request.POST.get('description')
            material.type = self.request.POST.get('type')
            material.save()
            material = MaterialForm(self.request.POST).save(commit=False)
            #material.user = user
            material.save()
        messages.success(self.request, '%s添加成功' % material)
        return redirect(self.success_url)


class MaterialUpdateView(UpdateView):
    form_class = MaterialForm
    template_name = 'masterdata/material/modal.html'
    success_url = '/masterdata/material/'
    context_object_name = 'spec_material'

    def get_object(self, queryset=None):
        return Material.objects.get(id=self.kwargs['material'])

    def get_context_data(self, **kwargs):
        context = super(MaterialUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_material', kwargs={'material': self.object.id})
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            material = Material.objects.get(id=self.kwargs['material'])
            material.groups = Group.objects.filter(id__in=self.request.POST.getlist('groups'))
            material.name = self.request.POST.get('name')
            material.description = self.request.POST.get('description')
            material.type = self.request.POST.get('type')
            #material.user = user
            material.save()
            MaterialForm(self.request.POST, instance=material).save()
        messages.success(self.request, '%s修改成功' % material)
        return redirect(self.success_url)


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = '/masterdata/material/'
    template_name = 'common/delete.html'

    def get_object(self, queryset=None):
        return Material.objects.get(id=self.kwargs['material'])

    def get_context_data(self, **kwargs):
        context = super(MaterialDeleteView, self).get_context_data(**kwargs)
        context['url'] = reverse('delete_material', kwargs={'material': self.object.id})
        return context

    def delete(self, request, *args, **kwargs):
        material = Material.objects.get(id=self.kwargs['material'])
        material.is_active = 0
        material.save()
        messages.success(self.request, '删除成功')
        return redirect(self.success_url)