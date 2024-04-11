from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegisterForm , VerifyCodeForm
import random
from help_utils import send_otp_code
from .models import otpCode , User , Team_Member
from django.contrib import messages

# Create your views here.



class RegisterView(View) :

    form_class = UserRegisterForm

    def get(self ,request )  :
        content = {
            'form': self.form_class() ,
        }

        return render(request,'accounts/signup.html' , content )

    def post(self , request ) :
        form = self.form_class(request.POST)
        if form.is_valid() :
            random_code = random.randint(1000 , 9999 )
            send_otp_code( form.cleaned_data['phone'] , random_code )

            new_otpcode = otpCode(phone_number=form.cleaned_data['phone'] , code=random_code)
            new_otpcode.save()
            request.session['user_registeration_info'] = {
                'phone' : form.cleaned_data['phone'] ,
                'email' : form.cleaned_data['email'] ,
                'full_name' : form.cleaned_data['full_name'] ,
                'password'  : form.cleaned_data['password']
            }

            messages.success(request, 'کد به شماره تلفن شما ارسال شد' , 'success' )
            return redirect('accounts:verify_code' )

        return render(request, 'accounts/signup.html', {'form':self.form_class()})

class VerifyCodeView(View) :

    form_class = VerifyCodeForm


    def get(self , request ) :
        return render(request,'accounts/verifycode.html' , {'form': self.form_class()})

    def post(self , request) :
        user_session = request.session['user_registeration_info']
        code_instance = otpCode.objects.filter(phone_number = user_session['phone'] ).first()

        form = self.form_class(request.POST)

        if form.is_valid() :
            code = form.cleaned_data['code']

            if code == code_instance.code :
                User.objects.create_user(email = user_session['email'], phone_number= user_session['phone'] , full_name = user_session['full_name'] , password=user_session['password'])
                code_instance.delete()
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد '  , 'success')
                return redirect('home:home')

            else :
                messages.error(request , 'کد وارد شده صحیح نمیباشد' , 'error')
                return redirect('accounts:verify_code')

        else :
            return redirect('home:home')



class TeamProfileView(View) :

    template_name = 'accounts/instructors-single.html'


    def setup(self, request, *args, **kwargs):
        self.teammember_profile = Team_Member.objects.get(id = kwargs['id'] )


        return super().setup(request, *args, **kwargs)

    def get(self, request , id ):
        content = {'team_member_profile': self.teammember_profile }
        return render(request, self.template_name, content  )

    def post(self, request , id ):
        content = {'team_member_profile': self.teammember_profile }
        return render(request, self.template_name, content  )
