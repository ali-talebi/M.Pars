
from django import  forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور' , 'class': 'form-control'}))
    password2 = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور' , 'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name' , 'picture' ]

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password1'] != cd['password2'] and cd['password1'] and cd ['password1'] :
            raise ValidationError("رمز عبور با تایید آن یکسان نیست")

        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text="<a href=\"../password/\"> شما میتوانید با فشردن روی این جمله رمز عبور خود را تغییر بدهید </a>")
    class Meta :
        model = User
        fields = [ 'email' , 'phone_number', 'full_name' , 'password' , 'picture' , 'last_login']






class UserRegisterForm(forms.Form):

    email     = forms.EmailField( label="ایمیل" , widget=forms.EmailInput())
    full_name = forms.CharField(  label='نام و نام خانوادگی', widget=forms.TextInput())
    phone     = forms.CharField( label = 'شماره تلفن', max_length=11)
    password  = forms.CharField(widget=forms.PasswordInput() , label="رمز عبور" )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user :
            raise ValidationError("این ایمیل از قبل موجود است")

        return email


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user  = User.objects.filter(phone_number=phone).exists()
        if user :
            raise ValidationError('این شماره تلفن قبلا ثبت نام شده است')
        return phone

class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()



class LoginForm(forms.Form):
    phone    = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


