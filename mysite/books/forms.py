from django import forms
from .models import Task

class TasksForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','desciption','important']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desciption':forms.Textarea(attrs={'class':'form-control'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }
    
                