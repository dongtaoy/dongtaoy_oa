# coding=utf-8
from django.forms import ModelForm
from masterdata.models import Material, MaterialType


class MaterialTypeForm(ModelForm):
    class Meta:
        model = MaterialType
        fields = '__all__'
        labels = {
            'name': '名称',
            'description': '描述'
        }


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        exclude = ['regtime', 'user']
        labels = {
            'name': '名称',
            'description': '描述',
            'type': '类型',
            'groups': '隶属于'
        }