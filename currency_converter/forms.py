from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserAuthForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, widget=forms.PasswordInput, label='Password')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2')


CURR_CHOICES = [('BYN', 'BYN'),
                ('RUB', 'RUB'),
                ('USD', 'USD'),
                ('EUR', 'EUR')]

class CurrencyForm(forms.Form):
    source_currency_value = forms.IntegerField(label='Amount', min_value=1)
    source_currency_code = forms.CharField(label='From', widget = forms.Select(choices=CURR_CHOICES))
    target_currency_code = forms.CharField(label='To', widget = forms.Select(choices=CURR_CHOICES))
