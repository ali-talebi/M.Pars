from django.shortcuts import render
from django.views import View
# Create your views here.



class CartView(View) :

    template_name = "orders/shop-cart.html"

    def get(self, request ):
        content = {}
        return render(request, self.template_name , content )


    def post(self, request) :
        content = {}
        return render(request, self.template_name , content )






