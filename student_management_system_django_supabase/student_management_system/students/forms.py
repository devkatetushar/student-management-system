from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("student_id", "full_name", "email", "course", "year", "phone")
        widgets = {
            "student_id": forms.TextInput(attrs={"placeholder": "e.g. CHEM2026-01"}),
            "full_name": forms.TextInput(attrs={"placeholder": "Student full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "student@example.com"}),
            "course": forms.TextInput(attrs={"placeholder": "e.g. Chemical Engineering"}),
            "year": forms.NumberInput(attrs={"min": "1", "max": "8"}),
            "phone": forms.TextInput(attrs={"placeholder": "Optional phone number"}),
        }
