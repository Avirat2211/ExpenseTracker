from django.forms import ModelForm
from .models import Expense
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount','category')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email