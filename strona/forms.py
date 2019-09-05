from django import forms


class loginForm(forms.Form):
    login = forms.CharField(label='Your everlasting')
    password = forms.CharField(widget=forms.PasswordInput(), label='Your password')