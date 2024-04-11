from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User
from django.urls import reverse
from django_jalali.db import models as django_jalali_models
from django.utils import timezone
# Create your models here.


class Course_Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام دسته بندی دوره های وبسایت")
    slug = models.SlugField(verbose_name="آدرس اینترنتی وبسایت" , unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Course_Category'
        verbose_name_plural = 'دسته بندی های دوره های وبسایت'




class Course_Tag(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام تگ")
    slug = models.SlugField( help_text="فیلد به طور خودکار مقدار دهی میشود" , verbose_name="آدرس اینترنتی تگ" , unique=True )
    color = models.CharField(max_length=100 , verbose_name="رنگ" , choices=[('bg-red-1', 'قرمز' ) , ('bg-white-1','سفید') , ('bg-dark-1','مشکی') ] , default='red' )
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Course_Tag'
        verbose_name_plural = 'تگ های دوره های وبسایت'
class Course_Information(models.Model):
    course_name = models.CharField(max_length=100 , verbose_name="نام دوره")
    picture = models.FileField(verbose_name="عکس اول" , upload_to=f'Course_Information/{course_name}/%y/%m/%d' , null = True )
    intoduce_centense = models.CharField(max_length=100 , null=True ,verbose_name="توضیح خیلی مختصر")
    category = models.ForeignKey(Course_Category , on_delete=models.CASCADE , verbose_name="نام دسته بندی")
    tags     = models.ManyToManyField(Course_Tag  , null=True , verbose_name="تگ های دوره های وبسایت")
    course_description = RichTextField(verbose_name="توضیحات دوره")
    learning = RichTextField(verbose_name="آنچه یادمیگیرید" )
    requirements = RichTextField(verbose_name="پیش نیاز های دوره")
    teacher = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="مدرس" , related_name="course_information")
    teacher_description = RichTextField(verbose_name="توضیحات درباره مدرس ")
    teacher_description_about_course = RichTextField(verbose_name="توضیحات مدرس درباره دوره" , null=True )
    video = models.FileField(verbose_name="ویدیو مقدمه انتشار دوره" , upload_to=f'Course_Information/{course_name}/%y/%m/%d' )
    price = models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name="قیمت دوره" )
    level = models.CharField(max_length=100 , verbose_name="سطح دوره" )
    languages = models.CharField(max_length=100 , verbose_name="زبان دوره")
    exam      = models.BooleanField(  verbose_name= "امتحان دارد" , default=False )
    duration  = models.IntegerField(verbose_name="مدت دوره" , default=35 )
    certificated = models.BooleanField(verbose_name="آیا مدرک دارد" , default=False )
    time = django_jalali_models.jDateTimeField(verbose_name= "زمان ساخت" , default=timezone.now  , null =True )
    update = django_jalali_models.jDateTimeField(verbose_name="زمان آپدیت" , auto_now=True)
    def get_absolute_url(self):
        return reverse("course:course_detail" , args=[str(self.id)])


    def __str__(self):
        return self.course_name

    class Meta:
        db_table = 'Course_Information'
        verbose_name_plural = 'دوره های وبسایت'


class Course_Comments(models.Model):
    course = models.ForeignKey(Course_Information , related_name='course_comments' , on_delete=models.CASCADE , verbose_name="دوره آموزشی")
    person = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="کاربر")
    title  = models.CharField(max_length=100 ,verbose_name="عنوان")
    text = models.TextField(verbose_name="متن کامنت برای دوره")

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'Course_Comments'
        verbose_name_plural = 'کامنت های دوره ها'