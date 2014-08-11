# encoding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from hr.models import Employee
from hr.forms import EmployeeForm


class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    template_name = 'hr/employee/modal.html'
    success_url = '/hr/employee/'

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_employee')
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            user = User.objects.create_user(self.request.POST.get('username'),
                                            self.request.POST.get('email'),
                                            self.request.POST.get('password1'))
            user.groups = Group.objects.filter(id__in=self.request.POST.get('groups'))
            user.last_name = self.request.POST.get('last_name')
            user.first_name = self.request.POST.get('first_name')
            user.save()
            employee = EmployeeForm(self.request.POST).save(commit=False)
            employee.user = user
            employee.save()
        messages.success(self.request, '%s添加成功' % employee)
        return redirect(self.success_url)


class EmployeeUpdateView(UpdateView):
    form_class = EmployeeForm
    template_name = 'hr/employee/modal.html'
    success_url = '/hr/employee/'
    context_object_name = 'spec_employee'
    pk_url_kwarg = 'employee'
    model = Employee

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_employee', kwargs={'employee': self.object.id})
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            employee = Employee.objects.get(id=self.kwargs['employee'])
            employee.user.groups = Group.objects.filter(id__in=self.request.POST.getlist('groups'))
            employee.user.last_name = self.request.POST.get('last_name')
            employee.user.first_name = self.request.POST.get('first_name')
            employee.user.email = self.request.POST.get('email')
            employee.user.save()
            EmployeeForm(self.request.POST, instance=employee).save()
        messages.success(self.request, '%s修改成功' % employee)
        return redirect(self.success_url)


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/hr/employee/'
    template_name = 'common/delete.html'
    pk_url_kwarg = 'employee'

    def delete(self, request, *args, **kwargs):
        user = Employee.objects.get(id=self.kwargs['employee']).user
        user.is_active = 0
        user.save()
        messages.success(self.request, '删除成功')
        return redirect(self.success_url)




# # delete user
# @permission_required('hr.employee_delete')
# def user_delete(request):
#     user = Employee.objects.get(id=request.POST.get('user_id')).user
#     user.is_active = 0
#     user.save()
#     return redirect('/hr/employee')


# check username existence
def user_check(request):
    try:
        User.objects.get(username=request.POST.get('username'))
        return HttpResponse('{"valid": false}')
    except:
        return HttpResponse('{"valid": true}')

