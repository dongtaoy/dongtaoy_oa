# encoding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from crm.models import Customer
from crm.forms import CustomerForm


class CustomerCreateView(SuccessMessageMixin, CreateView):
    form_class = CustomerForm
    template_name = 'crm/customer/modal.html'
    success_url = '/crm/customer/'
    success_message = '添加成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(CustomerCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_customer')
        return context




class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CustomerForm
    template_name = 'crm/customer/modal.html'
    success_url = '/crm/customer/'
    context_object_name = 'spec_customer'
    success_message = '修改成功'.decode('utf-8')
    model = Customer
    queryset = None
    pk_url_kwarg = 'customer'

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_customer', kwargs={'customer': self.object.id})
        return context


class CustomerDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/crm/customer/'
    model = Customer
    pk_url_kwarg = 'customer'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '删除成功')
        return super(CustomerDeleteView, self).delete(self.request, *args, **kwargs)
