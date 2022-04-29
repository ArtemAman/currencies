from django.urls import path
from currency_converter.views import CurrencyMain, CurrencyProfile, CurrencyAuth, CurrencyOutView, CurrencyRegestration

urlpatterns = [
    path('currency', CurrencyMain.as_view(), name='currency'),
    path('currency/myprofile', CurrencyProfile.as_view(), name='currency_profile'),
    path('currency/login', CurrencyAuth.as_view(), name='currency_auth'),
    path('currency/logout', CurrencyOutView.as_view(), name='currency_out'),
    path('currency/registration', CurrencyRegestration.as_view(), name='currency_registration'),

    # path('currency/<int:product_id>', views.ProductDetail.as_view(), name='product_detail'),
    # path('currency/cart', views.cart_detail, name='cart_detail'),
    # path('cart_add/<int:product_id>', views.cart_add, name='cart_add'),
    # path('cart_remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    # path('checkout', views.checkout, name='checkout'),
    # path('currency/myprofile/statistics', views.Statistics.as_view(), name='statistics'),

]