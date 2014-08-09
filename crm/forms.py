# coding=utf-8
from django.forms import ModelForm
from crm.models import Customer,CustomerType

class CustomerTypeForm(ModelForm):
    class Meta:
        model = CustomerType
        fields = '__all__'
        labels = {
            'name': '名称',
            'css': '样式',
            'description': '描述'
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'name': '名称',
            'phone': '电话',
            'address': '地址',
            'email': '邮箱',
            'fax': '传真',
            'type': '类型',
            'group': '隶属于'
        }