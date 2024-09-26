from django import forms
from .models import Employee_info

class Employee_infoForm(forms.ModelForm):
    class Meta:
        model=Employee_info
        
        fields="__all__"
        
        # widget={
        #     'description': forms.
        # }
        salary = forms.IntegerField(widget=forms.NumberInput(attrs={"readonly": "readonly"}))
        designation = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly",'style':'width:100%;height:10px'}))


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model=Employee_info
        fieldes="__all__"
        exclude=['salary','designation']
        