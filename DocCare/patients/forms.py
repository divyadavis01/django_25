from django import forms
from patients.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=[
        "name",
        "dob",
        'gender',
        'phone',
        'address',
        ]
        widgets={
            "dob":forms.DateInput(attrs={"type":"date"})
        }