from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    """
    Модель хранения данных о курсе валют
    """

    BYN = models.FloatField(default=1)
    RUB = models.FloatField()
    USD = models.FloatField()
    EUR = models.FloatField()
    time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return 'current currencies'



class UserProfile(models.Model):
    """ Модель пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class History(models.Model):
    """ Модель истории"""

    customer = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField()
    source_amount = models.FloatField()
    source_money = models.CharField(max_length=3, verbose_name='source_money')
    target_amount = models.FloatField()
    target_money = models.CharField(max_length=3, verbose_name='target_money')


    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'