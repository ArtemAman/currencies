
from django.utils import timezone

from currency.forms import UserAuthForm, RegisterForm, CurrencyForm
from currency.models import UserProfile, Currency, History
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from currency.helpers import get_request, refresh_currency


class CurrencyMain(View):
    """Представление главной страницы магазина, отображение всех доступных товаров во всех магазинах"""

    def get(self, request):
        dict_with_curr = get_request()
        refresh_currency(dict_with_curr)
        info_from_database = Currency.objects.first()
        currency_form = CurrencyForm()
        context = {'currencies': info_from_database,
                   'currency_form': currency_form}
        return render(request, 'currency/currency-index.html', context)

    def post(self, request):
        info_from_database = Currency.objects.first()
        currency_form = CurrencyForm(request.POST)
        context = {'currencies': info_from_database,
                   'currency_form': currency_form,
                   }
        if currency_form.is_valid():
            dict_from_base = {'RUB': info_from_database.RUB, 'BYN': info_from_database.BYN,
                              'USD': info_from_database.USD, 'EUR': info_from_database.EUR}
            source_currency_code = currency_form.cleaned_data['source_currency_code']
            target_currency_code = currency_form.cleaned_data['target_currency_code']
            input_currency_value = currency_form.cleaned_data['source_currency_value']

            from_country_base_value = dict_from_base[source_currency_code]
            to_country_base_value = dict_from_base[target_currency_code]

            converted_currency = (from_country_base_value / to_country_base_value) * float(input_currency_value)
            converted_currency = round(converted_currency, 2)
            context['converted_currency'] = converted_currency
            context['source_currency_code'] = source_currency_code
            context['input_currency_value'] = input_currency_value
            context['target_currency_code'] = target_currency_code
            user_profile = UserProfile.objects.get(user=request.user)
            History.objects.create(time=timezone.now(),
                                   source_amount=input_currency_value,
                                   source_money=source_currency_code,
                                   target_amount=converted_currency,
                                   target_money=target_currency_code,
                                   customer=user_profile,
                                   )

            return render(request, 'currency/currency-index.html', context)


class CurrencyRegistration(View):
    """Пердставление регистрации пользователя"""

    def get(self, request):
        reg_form = RegisterForm()
        context = {'reg_form': reg_form}
        return render(request, 'currency/registration.html', context)

    def post(self, request):
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()

            UserProfile.objects.create(user=user)
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context = {'reg_form': reg_form}
            return render(request, 'currency/registration.html', context)


class CurrencyAuth(LoginView):
    """Представление аутентификации пользователя на сайте"""

    def get(self, request, *args, **kwargs):
        auth_form = UserAuthForm()
        context = {'auth_form': auth_form}
        return render(request, 'currency/login.html', context)

    def post(self, request, *args, **kwargs):
        auth_form = UserAuthForm(request.POST)
        context = {'auth_form': auth_form}
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    auth_form.add_error(None, 'Ошибка! Учетная запись пользователя не активна!')
                    return render(request, 'currency/login.html', context)
            else:
                auth_form.add_error(None, 'Ошибка! Введен неправильный логин или пароль')
                return render(request, 'currency/login.html', context)


class CurrencyOutView(LogoutView):
    """Представление выхода из аккаунта пользователя на сайте"""

    next_page = '/'


class CurrencyProfile(View):
    """Представление профиля пользователя"""

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        history = History.objects.all().filter(customer=user_profile)
        context = {
            'user_profile': user_profile,
            'history': history,
        }
        return render(request, 'currency/myprofile.html', context)
