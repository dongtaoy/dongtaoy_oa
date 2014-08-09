from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from crm.forms import CustomerTypeForm, CustomerForm
from crm.models import Customer, CustomerType
from system.models import Label

class CustomerTypeCreateView(CreateView):
    form_class = CustomerTypeForm
    template_name = 'crm/customer/type/modal.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerTypeCreateView, self).get_context_data(**kwargs)
        context['url'] = '/crm/customer/type/ajax/add/'
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'crm/customer/type/body.html', {'labels': Label.objects.all(),'types': CustomerType.objects.all(),
                                                               'success': True})


class CustomerTypeUpdateView(UpdateView):
    form_class = CustomerTypeForm
    template_name = 'crm/customer/type/modal.html'
    context_object_name = 'spec_type'

    def get_object(self, queryset=None):
        return Label.objects.get(id=self.kwargs['label'])

    def get_context_data(self, **kwargs):
        context = super(CustomerTypeUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/crm/customer/type/ajax/mod/%d/' % self.object.id
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'crm/customer/type/body.html', {'labels': Label.objects.all(),'types': CustomerType.objects.all(),
                                                               'success': True})


@permission_required('crm.delete_type')
def type_delete(request):
    CustomerType.objects.get(id=request.POST.get('type_id')).delete()
    types = CustomerType.objects.all()
    labels = Label.objects.all()
    return render(request, 'crm/customer/type/body.html', {'labels': labels,'types': types,
                                                      'success': True})