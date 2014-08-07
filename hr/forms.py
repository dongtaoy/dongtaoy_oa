# coding=utf-8
from django.forms import ModelForm
from hr.models import Employee, Department, UserStatus


class UserStatusForm(ModelForm):
    class Meta:
        model = UserStatus
        fields = '__all__'
        labels = {
            'name': '名称',
            'description': '描述',
            'label': '标签'
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']
        fields = '__all__'
        labels = {
            'sex': '性别',
            'phone': '电话',
            'salary': '薪资',
            'description': '描述',
            'position': '职位',
            'dob': '生日',
            'identifier': '身份证号',
            'address': '地址',
            'status': '状态',
        }


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        exclude = ['group']
        fields = '__all__'
        labels = {
            'description': '描述',
            'leader': '领导',
            'label': '标签'
        }