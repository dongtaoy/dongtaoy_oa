from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView
from hr.models import Employee
from hr.forms import EmployeeForm


# # user index
# def user_index(request):
# return render(request, 'hr/employee/index.html', {'users': [x for x in Employee.objects.all() if x.user.is_active]},
# context_instance=RequestContext(request, processors=[common_context]))


class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    template_name = 'hr/employee/modal.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['url'] = '/hr/employee/ajax/add/'
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
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
        return render(self.request, 'hr/employee/body.html',
                      {"users": [x for x in User.objects.all() if x.is_active],
                       "success": True})


class EmployeeUpdateView(UpdateView):
    form_class = EmployeeForm
    template_name = 'hr/employee/modal.html'
    context_object_name = 'spec_employee'

    def get_object(self, queryset=None):
        return Employee.objects.get(id=self.kwargs['employee'])

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/hr/employee/ajax/mod/%d/' % self.object.id
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        employee = Employee.objects.get(id=self.kwargs['employee'])
        employee.user.groups = Group.objects.filter(id__in=self.request.POST.getlist('groups'))
        employee.user.last_name = self.request.POST.get('last_name')
        employee.user.first_name = self.request.POST.get('first_name')
        employee.user.email = self.request.POST.get('email')
        employee.user.save()
        EmployeeForm(self.request.POST, instance=employee).save()
        return render(self.request, 'hr/employee/body.html',
                      {"users": [x for x in User.objects.all() if x.is_active],
                       "success": True})


# delete user
@permission_required('hr.employee_delete')
def user_delete(request):
    user = Employee.objects.get(id=request.POST.get('user_id')).user
    user.is_active = 0
    user.save()
    return render(request, 'hr/employee/body.html', {"users": [x for x in User.objects.all() if x.is_active],
                                                     "success": True})


# check username existence
def user_check(request):
    try:
        User.objects.get(username=request.POST.get('user_username'))
        return HttpResponse('{"valid": false}')
    except:
        return HttpResponse('{"valid": true}')

