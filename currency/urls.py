from django.urls import path
from currency.views import CurrencyMain, CurrencyProfile, CurrencyAuth, CurrencyOutView, CurrencyRegistration

urlpatterns = [
    path('', CurrencyMain.as_view(), name='convert_currency'),
    path('myprofile', CurrencyProfile.as_view(), name='currency_profile'),
    path('login', CurrencyAuth.as_view(), name='currency_auth'),
    path('logout', CurrencyOutView.as_view(), name='currency_out'),
    path('registration', CurrencyRegistration.as_view(), name='currency_registration'),
]