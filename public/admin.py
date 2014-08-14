from django.contrib import admin
from public.models import Message, MessageTo, MessageType

admin.site.register(Message)
admin.site.register(MessageType)
admin.site.register(MessageTo)