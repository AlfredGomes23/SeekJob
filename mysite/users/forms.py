from django import forms
from .models import Candidate, Recruiter


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            "photo",
            "phone_number",
            "dob",
            "gender",
            "address",
            "current_company",
            "current_role",
            "skills",
            "portfolio_link",
            "experience_on_field",
            "resume",
        ]
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file w-50 m-auto btn-outline-info'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'current_company': forms.TextInput(attrs={'class': 'form-control'}),
            'current_role': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'portfolio_link': forms.URLInput(attrs={'class': 'form-control'}),
            'experience_on_field': forms.NumberInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file w-50 m-auto btn-outline-info'}),
        }


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = [
            "photo",
            "dob",
            "gender",
            "address",
            "phone_number",
            "company_name",
            "company_phone_number",
            "established_year",
            "website",
            "tenure",
        ]
        widgets = {
            "photo": forms.ClearableFileInput(attrs={"class": "form-control-file w-50 m-auto btn-outline-info"}),
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "company_phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "established_year": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "tenure": forms.NumberInput(attrs={"class": "form-control"}),
        }
