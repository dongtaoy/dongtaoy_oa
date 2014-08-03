from django.db import models

class Label(models.Model):
    name = models.CharField(max_length='50', null=True, blank=True)
    css = models.CharField(max_length='50', null=True, blank=True)
