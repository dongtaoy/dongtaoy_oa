# encoding=utf-8
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from system.models import Sidebar
from system.forms import SidebarForm
from dongtaoy_oa.views import permission_tree


class SidebarListView(ListView):
    model = Sidebar
    template_name = 'system/permission/sidebar/index.html'
    context_object_name = 'permissions'

    def get_queryset(self):
        return permission_tree(Sidebar.objects.all())


class SidebarCreateView(SuccessMessageMixin, CreateView):
    form_class = SidebarForm
    template_name = 'system/permission/sidebar/modal.html'
    success_url = '/system/permission/sidebar/'
    success_message = '%(name)s保存成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(SidebarCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_sidebar')
        return context


class SidebarUpdateView(SuccessMessageMixin, UpdateView):
    form_class = SidebarForm
    template_name = 'system/permission/sidebar/modal.html'
    context_object_name = 'spec_sidebar'
    success_url = '/system/permission/sidebar/'
    success_message = '%(name)s修改成功'.decode('utf-8')

    def get_object(self, queryset=None):
        return Sidebar.objects.get(id=self.kwargs['sidebar'])

    def get_context_data(self, **kwargs):
        context = super(SidebarUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_sidebar', kwargs={'sidebar': self.object.id})
        return context



# delete permission
@permission_required('system.delete_sidebar', raise_exception=True)
def permission_delete(request):
    Sidebar.objects.get(id=request.POST.get("permission_id")).delete()
    all_permissions = Sidebar.objects.all()
    return render(request, 'system/permission/sidebar/body.html', {"permissions": permission_tree(all_permissions),
                                                           "success": 1})
