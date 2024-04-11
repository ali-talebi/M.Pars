from django.db import models
from accounts.models import User
from django_jalali.db import models as django_jalali_models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.



class Event_Information(models.Model):
    picture    = models.FileField(verbose_name="تصویر سر تیتر برای سایت" , upload_to='Event/Pictures/%Y/%m/%d')
    event_name = models.CharField(max_length=100 , verbose_name="نام رویداد را وارد کنید")
    location   = models.CharField(max_length=100 , verbose_name="محل برگزاری")
    time       = django_jalali_models.jDateTimeField(verbose_name="تاریخ و زمان برگزاری" )
    Presentors = models.ManyToManyField(User , verbose_name="اراپه دهندگان")
    text       = RichTextField(verbose_name="متن")
    learning   = RichTextField(verbose_name="آنچه یادمیگیرید" , null = True )
    requirements  = RichTextField(verbose_name= "پیشنیازهای رویداد" , null = True )
    price      = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name= "قیمت اصلی" )
    off        = models.BooleanField(verbose_name= "آیا تخفیف دارد" , default=False )
    price2     = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name= "قیمت تخفیف خورده" , null=True, blank=True  )


    def get_absolute_url(self):
        return reverse('Event:Event_Detail', args = [str(self.id)])

    def __str__(self):
        return self.event_name


    class Meta :
        db_table = 'Event_Information'
        verbose_name_plural = "رویداد های وبسایت"



class Event_Comment(models.Model):

    event  = models.ForeignKey(Event_Information , verbose_name="رویداد" , on_delete=models.CASCADE , related_name="event_comments" )
    Person = models.ForeignKey(User , verbose_name="کاربر" , on_delete=models.CASCADE , related_name="event_comments" )
    title  = models.CharField(max_length=100 ,verbose_name= "عنوان" )
    text   = models.TextField(verbose_name="متن کامنت برای رویداد" )
    time   = django_jalali_models.jDateTimeField(verbose_name="زمان" , auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta :
        db_table = 'Event_Comment'
        verbose_name_plural = "کامنت های رویداد ها"

        ordering = ['-id']