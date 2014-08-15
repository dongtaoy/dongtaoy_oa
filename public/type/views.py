# encoding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from public.models import MessageType
from system.forms import MessageTypeForm


class MessageTypeCreateView(SuccessMessageMixin, CreateView):
    form_class = MessageTypeForm
    template_name = 'public/message/type/modal.html'
    success_url = '/public/message/type/'
    success_message = '添加成功'.decode("utf-8")

    def get_context_data(self, **kwargs):
        context = super(MessageTypeCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_messagetype')
        return context


class MessageTypeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MessageTypeForm
    template_name = 'public/message/type/modal.html'
    success_url = '/public/message/type/'
    success_message = '修改成功'.decode('utf-8')
    context_object_name = 'spec_type'
    pk_url_kwarg = 'type'
    model = MessageType

    def get_context_data(self, **kwargs):
        context = super(MessageTypeUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_messagetype', kwargs={'type': self.object.id})
        return context


class MessageTypeDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/public/message/type/'
    pk_url_kwarg = 'type'
    model = MessageType

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "删除成功")
        return super(MessageTypeDeleteView, self).delete(self.request, *args, **kwargs)






