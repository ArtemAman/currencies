# Generated by Django 2.2.5 on 2022-05-28 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BYN', models.FloatField(default=1)),
                ('RUB', models.FloatField()),
                ('USD', models.FloatField()),
                ('EUR', models.FloatField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('source_amount', models.FloatField()),
                ('source_money', models.CharField(max_length=3, verbose_name='source_money')),
                ('target_amount', models.FloatField()),
                ('target_money', models.CharField(max_length=3, verbose_name='target_money')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='currency.UserProfile')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
    ]
