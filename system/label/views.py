# encoding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from system.models import Label
from system.forms import LabelForm


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'system/label/modal.html'
    success_url = '/system/label'
    success_message = '%(name)s添加成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(LabelCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_label')
        return context


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    form_class = LabelForm
    template_name = 'system/label/modal.html'
    context_object_name = 'spec_label'
    success_url = '/system/label'
    success_message = '%(name)s修改成功'.decode('utf-8')

    def get_object(self, queryset=None):
        return Label.objects.get(id=self.kwargs['label'])

    def get_context_data(self, **kwargs):
        context = super(LabelUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_label', kwargs={'label': self.object.id})
        return context


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'common/delete.html'
    success_url = '/system/label/'

    def get_object(self, queryset=None):
        return Label.objects.get(id=self.kwargs['label'])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "删除成功")
        return super(LabelDeleteView, self).delete(self.request, *args, **kwargs)
