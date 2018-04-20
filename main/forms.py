from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields= '__all__'


class VisitForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(),widget=forms.TextInput)
    class Meta:
        model = Visit
        fields= '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
            'time': forms.TimeInput(attrs={'class': 'timepicker','data-format': 'hh:mm:ss'}),
        }
        