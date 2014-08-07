# coding=utf-8
from django.forms import ModelForm
from system.models import Label, Sidebar

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'
        labels = {
            'name': '名称',
            'css': '样式'
        }


class SidebarForm(ModelForm):
    class Meta:
        model = Sidebar
        fields = '__all__'
