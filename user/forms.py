from django import forms 

from .models import User


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone', 'role']
        labels = {
            'password': 'گذر واژه',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control my-5', 'placeholder':'example1234@gmail.com'}),
            'phone': forms.NumberInput(attrs={'class':'form-control my-5', 'placeholder':'09123456789'}),
            'username': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'myusername'}),
            'password': forms.PasswordInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}),
            'first_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Ali'}),
            'last_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'alizadeh'}),
            'role': forms.Select(attrs={'class':'form-control my-5'}),
        }
