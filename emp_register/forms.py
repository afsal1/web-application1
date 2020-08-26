from django import forms
from emp_register.models import Emp_register
class Emp_form(forms.ModelForm):
    class Meta:
        model = Emp_register
        fields = "__all__"