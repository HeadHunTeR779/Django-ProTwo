from django import forms
from.models import User


class MyModelForm(forms.ModelForm):   #forms not linked with any model inherit from forms.Form
    #custom validations go here
    class Meta:
        model = User             #which model's form is it?
        fields = "__all__"  # or fields = [list of all the fields] or exclude = [list of fields to exclude]
