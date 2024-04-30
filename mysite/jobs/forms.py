from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "category",
            "job_type",
            "role",
            "details",
            "photo",
            "contact_number",
            "deadline",
            "salary",
            "vacancy",
            "gender",
            "location",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "job_type": forms.Select(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"}),
            "details": forms.Textarea(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control-file w-50 m-auto btn-outline-info"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "vacancy": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
        }


