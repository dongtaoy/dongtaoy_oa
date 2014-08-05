# coding=utf-8
from django.db import models
from django.forms import ModelForm, Textarea

USAGE_CHOICE = (
    ('1', '使用'),
    ('0', '闲置')
)


class Asset(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True, null=True)
    regtime = models.DateField()
    categories = models.ManyToManyField('administration.AssetCategory')
    group = models.ForeignKey('hr.Department', blank=True, null=True, on_delete=models.SET_NULL)
    usage = models.CharField(max_length=1, choices=USAGE_CHOICE)


class AssetCategory(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, on_delete=models.SET_NULL)


class AssetForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.fields['group'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['categories'].label_from_instance = lambda obj: "%s" % obj.name
        self.fields['categories'].help_text = ''

    class Meta:
        model = Asset
        exclude = ['regtime']
        labels = {
            'brand': '品牌',
            'model': '型号',
            'description': '描述',
            'categories': '类型',
            'group': '隶属于',
            'usage': '闲置',
        }


class AssetCategoryForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AssetCategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['label'].label_from_instance = lambda obj: "%s" % obj.name

    class Meta:
        model = AssetCategory
        fields = '__all__'
        labels = {
            'name': '名称',
            'description': '描述',
        }