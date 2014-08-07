from django.shortcuts import render
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView, UpdateView
from hr.models import Department
from hr.forms import DepartmentForm
from django.http import HttpResponse


class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = 'hr/department/modal.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context['url'] = '/hr/department/ajax/add/'
        return context

    def form_valid(self, form):
        group = Group.objects.create(name=self.request.POST.get('group_name'))
        department = DepartmentForm(self.request.POST).save(commit=False)
        department.group = group
        department.save()
        return render(self.request, 'hr/department/body.html', {"success": True,
                                                                "groups": Department.objects.all()})


class DepartmentUpdateView(UpdateView):
    form_class = DepartmentForm
    template_name = 'hr/department/modal.html'
    context_object_name = 'spec_department'

    def get_object(self, queryset=None):
        return Department.objects.get(id=self.kwargs['department'])

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/hr/department/ajax/mod/%d/' % self.object.id
        return context

    def form_valid(self, form):
        department = DepartmentForm(self.request.POST,
                                    instance=Department.objects.get(id=self.kwargs['department'])).save()
        department.group.name = self.request.POST.get('group_name')
        department.group.save()
        return render(self.request, 'hr/department/body.html', {"success": True,
                                                                "groups": Department.objects.all()})


def group_delete(request):
    department = Department.objects.get(id=request.POST.get('group_id'))
    department.group.delete()
    department.delete()
    groups = Department.objects.all()
    return render(request, 'hr/department/body.html', {"success": True,
                                                       "groups": groups})


def group_check(request):
    try:
        Group.objects.get(name=request.POST.get('group_name'))
        return HttpResponse('{"valid": false}')
    except:
        return HttpResponse('{"valid": true}')