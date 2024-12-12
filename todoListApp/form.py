from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_comfirm = forms.CharField(widget=forms.PasswordInput, label="Comfirm PassWord")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        password_confirm = clean_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return clean_data