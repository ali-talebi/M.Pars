from django.shortcuts import render , redirect
from django.http   import HttpResponse
from django.views  import View
from Event.models  import Event_Information
from course.models import Course_Information
from accounts.models import Team_Member
from .models import Slider
from weblog.models import Post_Weblog
from product.models import Product_Product
# Create your views here.


class Home(View) :

    def setup(self, request, *args, **kwargs):
        self.courses = Course_Information.objects.all()
        self.slides  = Slider.objects.all()
        self.teams   = Team_Member.objects.all()
        self.posts = Post_Weblog.objects.all()
        self.products = Product_Product.objects.all()
        return super().setup(request, *args, **kwargs)

    template_name = 'home-2.html'
    def get(self , request ) :
        content = {'events' : Event_Information.objects.all() ,
                   'courses' : self.courses ,
                   'slides':self.slides ,
                   'teams' : self.teams ,
                   'posts' : self.posts ,
                   'products':self.products}
        return render(request, self.template_name , content )


    def post(self ,request ) :
        content = {'events' : Event_Information.objects.all() ,
                   'courses' : self.courses ,
                   'slides':self.slides ,
                   'teams' : self.teams ,
                   'posts' : self.posts ,
                   'products':self.products}
        return render(request, self.template_name , content )


