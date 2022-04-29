from django.contrib import admin
from currency_converter.models import UserProfile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']



admin.site.register(UserProfile, ProfileAdmin)
# Register your models here.
