from system.models import Label, Sidebar, PermissionProfile
from django.contrib import admin
from public.models import MessageType

admin.site.register(Label)
admin.site.register(Sidebar)
admin.site.register(PermissionProfile)
