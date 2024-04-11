from django.shortcuts import render , redirect
from django.views import View
from .models import Category_Weblog , Post_Weblog , Comments_Weblog
from .forms import CommentForm
from django.contrib import messages
# Create your views here.

class TotalPostView(View) :
    template_name = 'weblog/blog-list-1.html'

    def setup(self, request ,  slug_field = None  , *args, **kwargs ):
        self.posts = Post_Weblog.objects.all()
        self.category_total = Category_Weblog.objects.all()
        if slug_field :
            self.category = self.category_total.get(slug = slug_field )
            self.posts = self.posts.filter(category = self.category )
        return super().setup(request, *args, **kwargs  )

    def get(self, request,  slug_field = None  , *args, **kwargs   ):
        content = {'category': self.category_total ,
                   'posts': self.posts }
        return render(request, self.template_name , content  )

    def post(self, request,  slug_field = None  ,  *args, **kwargs  ):

        content = {'category': self.category ,
                   'posts': self.posts}
        return render(request, self.template_name , content )


class DetailPostView(View) :

    template_name = 'weblog/blog-single.html'
    comment_form  =  CommentForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post_Weblog.objects.get(id = kwargs['id'])
        self.total_comment = Comments_Weblog.objects.filter(post = self.post_instance)
        self.four_same_posts    = Post_Weblog.objects.filter(category = self.post_instance.category)[:4]
        next_post     = Post_Weblog.objects.filter( id = kwargs['id'] +1  ).exists()
        if next_post:
            self.next_post = Post_Weblog.objects.filter( id = kwargs['id'] +1  )

        else :
            self.next_post = None

        pervious      = Post_Weblog.objects.filter( id = kwargs['id'] -1 ).exists()
        if pervious :
            self.pervious_post = Post_Weblog.objects.filter(id = kwargs['id'] -1 )

        else :
            self.pervious_post = None
        return super().setup(request , *args , **kwargs )


    def get(self, request, id ) :
        content = {'post': self.post_instance ,'pervious':self.pervious_post , 'next':self.next_post   , 'four_same_posts' : self.four_same_posts, 'total_comment':self.total_comment ,'comment_form': self.comment_form() }
        return render(request, self.template_name , content)


    def post(self, request, id ):

        if not request.user.is_authenticated :

            return redirect('account:user_register')

        else :
            self.form = self.comment_form(request.POST )

            if self.form.is_valid() :
                model_isntance = Comments_Weblog(post = self.post_instance , person = self.request.user ,
                                title = self.form.cleaned_data['title'] , text = self.form.cleaned_data['text'])
                model_isntance.save()
                messages.success(request , 'کامنت شما با موفقیت ثبت شد' , 'success' )
                return redirect('home:home' )

            else :
                messages.error(request ,  'در ثبت کامنت شما مشکلی داریم ' , 'error' )

                return redirect('weblog:detail' , id  )


        return redirect('weblog:detail' , id )









        content = {'post': self.post_instance , 'pervious':self.pervious_post , 'next':self.next_post    , 'four_same_posts' : self.four_same_posts , 'total_comment':self.total_comment , 'comment_form': self.comment_form()  }
        return render(request, self.template_name , content )