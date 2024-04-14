from django.urls import path
from .views import CartView

app_name = 'orders'
urlpatterns = [
    path('carts/', CartView.as_view(), name='carts'),
]