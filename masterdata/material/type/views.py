# encoding=utf-8
from django.contrib.auth.decorators import permission_required
from masterdata.forms import MaterialForm, MaterialTypeForm
from masterdata.models import MaterialType, Material
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
import time

class MaterialTypeCreateView(SuccessMessageMixin, CreateView):
    form_class = MaterialTypeForm
    template_name = 'masterdata/material/type/modal.html'
    success_url = '/masterdata/material/type/'
    success_message = '%(name)s添加成功'.decode("utf-8")

    def get_context_data(self, **kwargs):
        context = super(MaterialTypeCreateView, self).get_context_data(**kwargs)
        context['url'] = '/masterdata/material/type/ajax/add/'
        return context


class MaterialTypeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MaterialTypeForm
    template_name = 'masterdata/material/type/modal.html'
    success_url = '/masterdata/material/type/'
    success_message = '%(name)s修改成功'.decode('utf-8')
    context_object_name = 'spec_type'

    def get_object(self, queryset=None):
        return MaterialType.objects.get(id=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super(MaterialTypeUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/masterdata/material/type/ajax/mod/%d/' % self.object.id
        return context


class MaterialTypeDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/masterdata/material/type/'

    def get_object(self, queryset=None):
        return MaterialType.objects.get(id=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super(MaterialTypeDeleteView, self).get_context_data(**kwargs)
        context['url'] = reverse('delete_materialtype', kwargs={'type': self.object.id})
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "删除成功")
        return super(MaterialTypeDeleteView, self).delete(self.request, *args, **kwargs)