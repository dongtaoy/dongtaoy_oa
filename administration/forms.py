# coding=utf-8
from django.forms import ModelForm
from administration.models import Asset, AssetCategory


class AssetForm(ModelForm):
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
            'label': '标签'
        }