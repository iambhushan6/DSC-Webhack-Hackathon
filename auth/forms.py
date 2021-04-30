from django import forms

class Loginform(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput)