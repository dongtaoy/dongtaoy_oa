# encoding=utf-8
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from masterdata.models import Material
from masterdata.forms import MaterialForm
import time

class MaterialCreateView(SuccessMessageMixin, CreateView):
    form_class = MaterialForm
    template_name = 'masterdata/material/modal.html'
    success_url = '/masterdata/material/'

    def get_context_data(self, **kwargs):
        context = super(MaterialCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_material')
        return context

    def form_valid(self, form):
        super(MaterialCreateView, self).form_valid(form)
        self.object.regtime = time.strftime('%Y-%m-%d')
        self.object.save()
        return redirect(self.success_url)

    # def form_valid(self, form):
    #     print form
    #     #messages.success(self.request, '%s添加成功' % material)
    #     return redirect(self.success_url)


class MaterialUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MaterialForm
    template_name = 'masterdata/material/modal.html'
    success_url = '/masterdata/material/'
    context_object_name = 'spec_material'

    def get_object(self, queryset=None):
        return Material.objects.get(id=self.kwargs['material'])

    def get_context_data(self, **kwargs):
        context = super(MaterialUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_material', kwargs={'material': self.object.id})
        return context




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
        messages.success(self.request, '删除成功')
        return super(MaterialDeleteView, self).delete(self.request, *args, **kwargs)