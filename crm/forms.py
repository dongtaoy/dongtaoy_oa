# coding=utf-8
from django.forms import ModelForm
from crm.models import CustomerType,Customer

class CustomerTypeForm(ModelForm):
    class Meta:
        model = CustomerType
        fields = '__all__'
        labels = {
            'name': '名称',
            'description': '描述',
            'label': '标签'
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'name': '名称',
            'phone': '描述',
            'address': '标签',
            'email': '邮箱',
            'fax': '传真',
            'type': '类型',
            'groups': '隶属于'

        }