from django.urls import path
from .views import Total_Product , Detail_Product


app_name = 'product'
urlpatterns = [
    path('', Total_Product.as_view() , name="total_product" ) ,
    path('detail_product/<int:id>' , Detail_Product.as_view() , name="detail_product")

]