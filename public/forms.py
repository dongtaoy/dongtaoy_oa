# encoding=utf-8
from django.forms import ModelForm
from public.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['toUser', 'fromUser', 'type', 'time']
        fields = '__all__'
        labels = {
            'subject': '主题',
            'body': '内容'
        }