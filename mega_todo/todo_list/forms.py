from django import forms

class AddToDoForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your task'}))

class LogInForm(forms.Form):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username or email'}))
    password=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

class EditOneForm(forms.Form):
    name_task=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your task'}))
    done_task=forms.BooleanField()

class ResetPasswordForm(forms.Form):
    old_password=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type current password'}))
    new_password1=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type new password'}))
    new_password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))
