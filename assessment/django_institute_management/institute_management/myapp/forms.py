from django import forms
from .models import*

class signupForm(forms.ModelForm):
    class Meta:
        model=signupmodel
        fields="__all__"

class add_studentForm(forms.ModelForm):
    class Meta:
        model=add_student
        fields='__all__'        