from django.shortcuts import render
from django.db import transaction
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import permission_required
from system.models import Sidebar
from system.forms import SidebarForm
from dongtaoy_oa.views import permission_tree


class SidebarListView(ListView):
    model = Sidebar
    template_name = 'system/permission/index.html'
    context_object_name = 'permissions'

    def get_queryset(self):
        return permission_tree(Sidebar.objects.all())


class SidebarCreateView(CreateView):
    form_class = SidebarForm
    template_name = 'system/permission/modal.html'

    def get_context_data(self, **kwargs):
        context = super(SidebarCreateView, self).get_context_data(**kwargs)
        context['url'] = '/system/permission/ajax/add/'
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'system/permission/body.html',
                      {"permissions": permission_tree(Sidebar.objects.all()), "success": True})


class SidebarUpdateView(UpdateView):
    form_class = SidebarForm
    template_name = 'system/permission/modal.html'
    context_object_name = 'spec_sidebar'

    def get_object(self, queryset=None):
        return Sidebar.objects.get(id=self.kwargs['sidebar'])

    def get_context_data(self, **kwargs):
        context = super(SidebarUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/system/permission/ajax/mod/%d/' % self.object.id
        return context

    def form_valid(self, form):
        form.save()
        return render(self.request, 'system/permission/body.html',
                      {"permissions": permission_tree(Sidebar.objects.all()), "success": True})


# delete permission
@permission_required('system.delete_sidebar', raise_exception=True)
def permission_delete(request):
    Sidebar.objects.get(id=request.POST.get("permission_id")).delete()
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})
