from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control", "placeholder":"password"}))


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"first_name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"last_name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"phone_number"}))
    username = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"username"}))
    password = forms.CharField(widget=forms.PasswordInput({"class":"form-control", "placeholder":"password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class":"form-control", "placeholder":"password"}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number', 'username', 'password', 'confirm_password')


    def clean_data(self):
        password = self.clean_data['password']
        confirm_password = self.clean_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password
    

class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"first_name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"last_name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"phone_number"}))
    username = forms.CharField(widget=forms.TextInput({"class":"form-control", "placeholder":"username"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'username', 'user_role']