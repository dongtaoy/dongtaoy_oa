from django.forms import ModelForm
from hr.models import Employee, Department, UserStatus


class UserStatusForm(ModelForm):
    class Meta:
        model = UserStatus
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'