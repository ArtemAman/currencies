from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# dummy choices
CURR_CHOICES = [('BYN', 'BYN'),
                ('RUB', 'RUB'),
                ('USD', 'USD'),
                ('EUR', 'EUR')]

class CurrencyForm(forms.Form):
    source_currency_value = forms.DecimalField(label='Amount')
    source_currency_code = forms.CharField(label='From', widget = forms.Select(choices=CURR_CHOICES))
    target_currency_code = forms.CharField(label='To', widget = forms.Select(choices=CURR_CHOICES))


    # def __init__(self, tuple_country_code, *args, **kwargs):
    #     # required to set the initial form drop down with choices
    #     self.tuple_country_code = tuple_country_code
    #     super(CurrencyForm,self).__init__(*args, **kwargs)
    #
    #     self.fields['source_currency_code'].widget.choices = self.tuple_country_code
    #     self.fields['target_currency_code'].widget.choices = self.tuple_country_code


class UserAuthForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, widget=forms.PasswordInput, label='Password')

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
