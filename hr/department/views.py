# encoding=utf-8
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from hr.models import Department, Employee
from hr.forms import DepartmentForm
from django.http import HttpResponse


class DepartmentCreateView(SuccessMessageMixin, CreateView):
    form_class = DepartmentForm
    template_name = 'hr/department/modal.html'
    success_url = '/hr/department/'
    success_message = '添加成功'

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_department')
        context['form'].fields['leader'].queryset = Employee.objects.filter(user__is_active=1)
        return context

    def form_valid(self, form):
        with transaction.atomic():
            group = Group.objects.create(name=self.request.POST.get('group_name'))
            department = DepartmentForm(self.request.POST).save(commit=False)
            department.group = group
            department.save()
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = DepartmentForm
    template_name = 'hr/department/modal.html'
    success_url = '/hr/department/'
    context_object_name = 'spec_department'
    success_message = '修改成功'

    def get_object(self, queryset=None):
        return Department.objects.get(id=self.kwargs['department'])

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_department', kwargs={'department': self.object.id})
        context['form'].fields['leader'].queryset = Employee.objects.filter(user__is_active=1)
        return context

    def form_valid(self, form):
        with transaction.atomic():
            department = DepartmentForm(self.request.POST,
                                        instance=Department.objects.get(id=self.kwargs['department'])).save()
            department.group.name = self.request.POST.get('group_name')
            department.group.save()
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)


class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = '/hr/department/'
    template_name = 'common/delete.html'

    def get_object(self, queryset=None):
        return Department.objects.get(id=self.kwargs['department'])

    def get_context_data(self, **kwargs):
        context = super(DepartmentDeleteView, self).get_context_data(**kwargs)
        context['url'] = reverse('delete_department', kwargs={'department': self.object.id})
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '删除成功')
        Department.objects.get(id=self.kwargs['department']).group.delete()
        return redirect(self.success_url)


def group_check(request, department=None):
    try:
        inputgroup = Group.objects.get(name=request.POST.get('group_name'))
        try:
            department = int(department)
            print 'in'
            group = Department.objects.get(id=department)
            print 'group'
            if group.group == inputgroup:
                return HttpResponse('{"valid": true}')
            else:
                return HttpResponse('{"valid": false}')
        except:
            return HttpResponse('{"valid": false}')
    except:
        return HttpResponse('{"valid": true}')