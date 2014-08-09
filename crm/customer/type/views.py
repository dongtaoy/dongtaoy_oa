# encoding=utf-8
from django.contrib.auth.decorators import permission_required
from crm.forms import CustomerTypeForm, CustomerForm
from crm.models import Customer, CustomerType
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages


class CustomerTypeCreateView(SuccessMessageMixin, CreateView):
    form_class = CustomerTypeForm
    template_name = 'crm/customer/type/modal.html'
    success_url = '/crm/customer/type/'
    success_message = '%(name)s添加成功'.decode("utf-8")

    def get_context_data(self, **kwargs):
        context = super(CustomerTypeCreateView, self).get_context_data(**kwargs)
        context['url'] = '/crm/customer/type/ajax/add/'
        return context


class CustomerTypeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CustomerTypeForm
    template_name = 'crm/customer/type/modal.html'
    success_url = '/crm/customer/type/'
    success_message = '%(name)s修改成功'.decode('utf-8')
    context_object_name = 'spec_type'

    def get_object(self, queryset=None):
        return CustomerType.objects.get(id=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super(CustomerTypeUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/crm/customer/type/ajax/mod/%d/' % self.object.id
        return context


class CustomerTypeDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/crm/customer/type/'

    def get_object(self, queryset=None):
        return CustomerType.objects.get(id=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super(CustomerTypeDeleteView, self).get_context_data(**kwargs)
        context['url'] = reverse('delete_customertype', kwargs={'type': self.object.id})
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "删除成功")
        return super(CustomerTypeDeleteView, self).delete(self.request, *args, **kwargs)
