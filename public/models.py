from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=50)
    body = models.TextField(max_length=500, blank=True, null=True)
    fromUser = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='Message_fromUser')
    toUser = models.ManyToManyField('auth.User', through='MessageTo', blank=True, null=True,
                                    related_name='Message_toUser')
    type = models.ForeignKey('public.MessageType', blank=True, null=True)
    time = models.DateTimeField(null=True, blank=True)

    class Meta:
        permissions = (
        ('publish_announcement', 'Can publish announcement'), ('view_announcement', 'Can view announcement'),)


class MessageTo(models.Model):
    message = models.ForeignKey('public.Message', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    read = models.DateTimeField(null=True, blank=True)
    delete = models.DateTimeField(null=True, blank=True)


class MessageType(models.Model):
    category_choice = (
        ('S', 'System'),
        ('P', 'Private')
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=1, choices=category_choice)