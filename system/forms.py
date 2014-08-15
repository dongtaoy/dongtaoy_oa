# coding=utf-8
from django.forms import ModelForm
from system.models import Label, Sidebar
from public.models import MessageType

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'
        labels = {
            'name': '名称',
            'css': '样式'
        }


class SidebarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SidebarForm, self).__init__(*args, **kwargs)
        self.fields['permissions'].label_from_instance = lambda obj: "%s.%s" % (obj.content_type.app_label, obj.codename)
        self.fields['permissions'].help_text = ''

    class Meta:
        model = Sidebar
        fields = '__all__'
        labels = {
            'name': '名称',
            'order': '顺序',
            'parent': '父层',
            'permissions': '权限',
        }

class MessageTypeForm(ModelForm):
    class Meta:
        model = MessageType
        fields = '__all__'
        labels = {
            'name': '名称',
            'description': '描述',
            'category': '种类'
        }