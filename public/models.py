from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=500, blank=True, null=True)
    fromUser = models.ForeignKey('hr.Employee', blank=True, null=True, on_delete=models.SET_NULL, related_name='Message_fromUser')
    toUser = models.ManyToManyField('hr.Employee', through='MessageTo', blank=True, null=True, related_name='Message_toUser')
    type = models.ForeignKey('public.MessageType', blank=True, null=True)
    time = models.DateField(null=True, blank=True)


class MessageTo(models.Model):
    message = models.ForeignKey('public.Message', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('hr.Employee', null=True, blank=True, on_delete=models.SET_NULL)
    read = models.DateField(null=True, blank=True)
    delete = models.DateField(null=True, blank=True)


class MessageType(models.Model):
    category_choice = (
        ('S', 'System'),
        ('P', 'Private')
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=1, choices=category_choice)