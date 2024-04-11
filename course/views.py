from django.shortcuts import render , redirect
from .models import Course_Information
from django.views import View
from .forms import Course_CommentsForm
from django.contrib import messages
# Create your views here.



class Course_View(View):

    template_name = 'course/course.html'

    def setup(self, request, *args, **kwargs):
        self.course = Course_Information.objects.all()
        return super().setup(request, *args, **kwargs)


    def get(self , request ) :
        pass

    def post(self , request ) :
        pass


class Course_Detail_View(View):

    template_name = 'course/courses-single-2.html'
    form = Course_CommentsForm

    def setup(self , request , *args, **kwargs):
        self.course = Course_Information.objects.get(id = kwargs['id'] )
        self.like_course = Course_Information.objects.filter(category = self.course.category)
        return super().setup(request , *args, **kwargs)

    def get(self , request , id ):
        content = {'course' : self.course ,
                   'like_course' : self.like_course ,
                   'from':self.form()}
        return render(request, self.template_name, content )


    def post(self , request , id ) :

        form = self.form(request.POST )
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.course = self.course
            new_comment.person = self.request.user
            new_comment.save()
            messages.success(request , 'کامنت شما با موفقیت ثبت شد' , 'success')
            return redirect("course:course_detail", id)


        else :
            messages.error(request , 'کامنت شما ثبت نشد' , 'error')


        content = {'course' : self.course ,
                   'like_course' : self.like_course}
        return render(request, self.template_name, content )

