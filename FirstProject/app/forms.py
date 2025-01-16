from django import forms


class register_form(forms.Form):
    your_email = forms.CharField(label="Your email", max_length=30)
    your_password = forms.CharField(label="Your password", max_length=12)


class login_form(forms.Form):
    email = forms.CharField(label="email", max_length=30)
    password = forms.CharField(label="password", max_length=12)
