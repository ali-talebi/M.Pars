from django.db import models
from django.contrib.auth.models import AbstractBaseUser , AbstractUser
from .managers import UserManager
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractBaseUser):

    email = models.EmailField(unique=True , verbose_name= "ایمیل" )
    phone_number = models.CharField(verbose_name="شماره تلفن" , max_length=11 , unique=True)
    is_active    = models.BooleanField(verbose_name="آیا کاربر فعال است ؟" , default= True )
    is_admin     = models.BooleanField(verbose_name="آیا ادمین است ؟" , default=False      )
    full_name    = models.CharField(verbose_name="نام و نام کاربری" , max_length=50 )
    picture      = models.FileField(verbose_name= "تصویر کاربری" , upload_to="User/%Y/%m/%d" , blank= True , null = True )

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['email' , 'full_name' ]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.is_admin



class otpCode(models.Model):

    phone_number = models.CharField(max_length=11 , verbose_name="شماره تلفن")
    code = models.PositiveSmallIntegerField(verbose_name="کد تایید")
    creation = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.creation} '




class Skills(models.Model):
    name = models.CharField(verbose_name="نام مهارت" , max_length=15 )

    def __str__(self):
        return self.name
    class Meta :
        db_table = 'skills'
        verbose_name_plural = "مهارت های اعضا"

class Team_Member(models.Model):
    team_member = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="فرد")
    introduce   = models.CharField(verbose_name="معرفی نامه" )
    skills = models.ManyToManyField(Skills , null=True )
    description = RichTextField(verbose_name="توضیحات درباره معرفی جامع عضو تیم" , null=True, blank=True)
    @property
    def give_fulll_name(self):
        return self.team_member.full_name
    linkedin = models.CharField(verbose_name="لینکدین" , null=True, blank=True, max_length=50 )
    instagram = models.CharField(verbose_name="اینستاگرام" , null=True, blank=True, max_length=50 )


    def __str__(self):
        return self.team_member.full_name

    class Meta :
        db_table = 'team_member'
        verbose_name_plural = "اعضای تیم"