# encoding=utf-8
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from administration.models import Asset
from administration.forms import AssetForm
import time


class AssetCreateView(SuccessMessageMixin, CreateView):
    form_class = AssetForm
    template_name = 'administration/asset/modal.html'
    success_url = '/administration/asset/'
    success_message = '%(brand)s-%(model)s 添加成功'.decode('utf-8')

    def get_context_data(self, **kwargs):
        context = super(AssetCreateView, self).get_context_data(**kwargs)
        context['url'] = reverse('add_asset')
        return context

    def form_valid(self, form):
        super(AssetCreateView, self).form_valid(form)
        self.object.regtime = time.strftime('%Y-%m-%d')
        self.object.save()
        return redirect(self.success_url)


class AssetUpdateView(SuccessMessageMixin, UpdateView):
    form_class = AssetForm
    template_name = 'administration/asset/modal.html'
    success_url = '/administration/asset/'
    context_object_name = 'spec_asset'
    success_message = '%(brand)s-%(model)s 修改成功'.decode('utf-8')
    model = Asset
    queryset = None
    pk_url_kwarg = 'asset'

    def get_context_data(self, **kwargs):
        context = super(AssetUpdateView, self).get_context_data(**kwargs)
        context['url'] = reverse('change_asset', kwargs={'asset': self.object.id})
        return context


class AssetDeleteView(DeleteView):
    template_name = 'common/delete.html'
    success_url = '/administration/asset/'
    model = Asset
    pk_url_kwarg = 'asset'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '删除成功')
        return super(AssetDeleteView, self).delete(self.request, *args, **kwargs)
