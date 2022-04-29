

import json
import requests
from django.utils import timezone

from currency_converter.models import Currency

def get_request():
    list_of_currencies_we_interested = ['RUB', 'EUR', 'USD']
    dict_of_currencies = {}
    try:
        api_request = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0", timeout=10)
        currency_dict = json.loads(api_request.text)
        for element in currency_dict:
            if element['Cur_Abbreviation'] in list_of_currencies_we_interested:
                if element['Cur_Abbreviation'] == 'RUB':
                    dict_of_currencies[element['Cur_Abbreviation']] = element['Cur_OfficialRate'] / element['Cur_Scale']
                else:
                    dict_of_currencies[element['Cur_Abbreviation']] = element['Cur_OfficialRate']
    except Exception as exc:
        print(exc)
    return dict_of_currencies


def refresh_currency(dict_of_currencies):
    if len(dict_of_currencies) != 0:
        info_from_database = Currency.objects.all()
        if len(info_from_database) == 0:
            Currency.objects.create(RUB=dict_of_currencies['RUB'],
                                    USD=dict_of_currencies['USD'],
                                    EUR=dict_of_currencies['EUR'],
                                    time=timezone.now(),
                                    )
        else:
            Currency.objects.filter(id=1).update(
                RUB=dict_of_currencies['RUB'],
                USD=dict_of_currencies['USD'],
                EUR=dict_of_currencies['EUR'],
                time=timezone.now(),
            )





