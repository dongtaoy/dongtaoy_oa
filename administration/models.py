# coding=utf-8
from django.db import models
from django.forms import ModelForm, Textarea


class Asset(models.Model):
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    categories = models.ManyToManyField('administration.AssetCategory', blank=True, null=True)
    group = models.ForeignKey('hr.Group', blank=True, null=True, on_delete=models.SET_NULL)
    usage = models.BooleanField(blank=True, default=True)


class AssetCategory(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, on_delete=models.SET_NULL)


class AssetCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssetCategoryForm, self).__init__(*args, **kwargs)
        self.fields['label'].label_from_instance = lambda obj: "%s" % obj.name

    class Meta:
        model = AssetCategory
        fields = '__all__'
        labels = {
            'description': '描述',
        }