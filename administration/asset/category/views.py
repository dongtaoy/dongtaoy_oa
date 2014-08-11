# encoding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from administration.models import AssetCategory
from administration.forms import AssetCategoryForm


class AssetCategoryCreateView(SuccessMessageMixin, CreateView):
    form_class = AssetCategoryForm
    template_name = 'administration/asset/category/modal.html'
    success_url = '/administration/asset/category/'
    success_message = '%(name)s添加成功'.decode("utf-8")

    def get_context_data(self, **kwargs):
        context = super(AssetCategoryCreateView, self).get_context_data(**kwargs)
        context['url'] = '/administration/asset/category/ajax/add/'
        return context


class AssetCategoryUpdateView(SuccessMessageMixin, UpdateView):
    form_class = AssetCategoryForm
    template_name = 'administration/asset/category/modal.html'
    success_url = '/administration/asset/category/'
    success_message = '%(name)s修改成功'.decode('utf-8')
    context_object_name = 'spec_category'
    pk_url_kwarg = 'category'
    model = AssetCategory

    def get_context_data(self, **kwargs):
        context = super(AssetCategoryUpdateView, self).get_context_data(**kwargs)
        context['url'] = '/administration/asset/category/ajax/mod/%d/' % self.object.id
        return context


class AssetCategoryDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/administration/asset/category/'
    pk_url_kwarg = 'category'
    model = AssetCategory

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "删除成功")
        return super(AssetCategoryDeleteView, self).delete(self.request, *args, **kwargs)






