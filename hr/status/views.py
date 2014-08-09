# encoding=utf-8
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from hr.models import UserStatus
from hr.forms import UserStatusForm
from system.models import Label


class UserStatusCreateView(SuccessMessageMixin, CreateView):
    form_class = UserStatusForm
    template_name = 'hr/status/modal.html'
    success_url = '/hr/status/'
    success_message = '%(name)s 添加成功成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(UserStatusCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_userstatus')
        return context


class UserStatusUpdateView(SuccessMessageMixin, UpdateView):
    form_class = UserStatusForm
    template_name = 'hr/status/modal.html'
    success_url = '/hr/status/'
    success_message = '%(name)s 添加成功成功'.decode('utf-8')
    context_object_name = 'spec_userstatus'

    def get_object(self, queryset=None):
        return UserStatus.objects.get(id=self.kwargs['status'])

    def get_context_data(self, **kwargs):
        context = super(UserStatusUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_userstatus', kwargs={'status': self.object.id})
        return context


class UserStatusDeleteView(DeleteView):
    model = UserStatus
    success_url = '/hr/status/'

    def get_object(self, queryset=None):
        return UserStatus.objects.get(id=self.kwargs['status'])

    def get_context_data(self, **kwargs):
        context = super(UserStatusDeleteView, self).get_context_data(**kwargs)
        context['url'] = reverse('delete_userstatus', kwargs={'status': self.object.id})
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request)
        return super(UserStatusDeleteView, self).delete(self.request, *args, **kwargs)


def userstatus_detail(request):
    labels = Label.objects.all()
    try:
        spec_userstatus = UserStatus.objects.get(id=request.GET.get('userstatus_id'))
    except Exception, e:
        spec_userstatus = None
    return render(request, 'hr/status/modal.html', {'spec_userstatus': spec_userstatus,
                                                    'labels': labels})


def userstatus_save(request):
    UserStatus(id=request.POST.get('userstatus_id'),
               name=request.POST.get('userstatus_name'),
               description=request.POST.get('userstatus_description'),
               label=Label.objects.get(id=request.POST.get('userstatus_label'))).save()
    userstatuses = UserStatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})


def userstatus_delete(request):
    UserStatus.objects.get(id=request.POST.get('userstatus_id')).delete()
    userstatuses = UserStatus.objects.all()
    return render(request, 'hr/status/body.html', {'userstatuses': userstatuses,
                                                   'success': 1})