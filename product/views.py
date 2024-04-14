from django.shortcuts import render
from .models import Product_Product , Category_Product , Tag_Product
from django.views import View
from orders.forms import CartAddForm
# Create your views here.






class Total_Product(View):

    template_name = 'product/shop-list.html'

    def setup(self, request , product_slug =None, *args , **kwargs):
        self.total_product  = Product_Product.objects.all()
        self.total_category = Category_Product.objects.all()

        if product_slug:
            self.total_category = self.total_category.filter(slug=product_slug)
            self.total_product = self.total_product.filter(slug = self.total_category )

        return super().setup(request , *args , **kwargs )




    def get(self, request , product_slug=None  ):

        content = {'total_product' : self.total_product ,
                   'total_category' : self.total_category ,
                   'add_form' : CartAddForm() ,
                   }
        return render(request , self.template_name , content )


    def post(self, request , product_slug=None ):
        content = {'total_product' : self.total_product ,
                   'total_category' : self.total_category ,
                   'form' : CartAddForm() ,
                   }
        return render(request , self.template_name , content )



class Detail_Product(View) :

    template_name = 'product/shop-single.html'

    def setup(self, request, *args, **kwargs):
        self.product = Product_Product.objects.get(id=kwargs['id'])
        self.like_products = Product_Product.objects.filter(category = self.product.category and id != self.product.id )[:4]
        return super().setup(request , *args , **kwargs )


    def get(self , request , id ):
        content = {'product': self.product , 'like_products': self.like_products }
        return render(request , self.template_name , content )

    def post(self , request , id ):
        content = {'product': self.product , 'like_products': self.like_products }
        return render(request , self.template_name , content )