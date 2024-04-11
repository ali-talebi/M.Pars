from django.db import models
from accounts.models import User
from .managers import Weblog_Manager
from ckeditor.fields import RichTextField
from django.urls import reverse
from django_jalali.db import models as django_jalali_models
# Create your models here.


class Category_Weblog(models.Model):

    category_name = models.CharField(max_length=100 , verbose_name="نام دسته بندی ")
    slug = models.SlugField(verbose_name="آدرس اینترنتی دسته بندی" , help_text="این فیلد به طوری خودکار مقدار دهی میشود" , unique=True)


    def get_absolute_url(self):
        return reverse('weblog:Total_Post' , args=[self.slug])


    def __str__(self):
        return self.category_name

    class Meta :
        db_table = 'Category_Weblog'
        verbose_name_plural = "دسته بندی پست های وبلاگ"




class Tags_Weblog(models.Model) :
    tag_name = models.CharField(max_length=100  , verbose_name="تگ برای پست های وبلاگ")
    slug     = models.SlugField(verbose_name= "آدرس اینترنتی برای تگ پست" , unique=True)

    def __str__(self):
        return self.tag_name

    class Meta :
        db_table = 'Tags_Weblog'
        verbose_name_plural = "تگ های پست های وبسایت"


class Post_Weblog(models.Model):
    picture = models.FileField(verbose_name="عکس مورد نظر", upload_to='Post_Weblog/%Y/%m/%d',null=True, blank=True)
    post_name = models.CharField(max_length=100 , verbose_name="عنوان پست ها")
    slug = models.SlugField(verbose_name="آدرس اینترنتی پست" , help_text="به طور خودکار مقدار دهی میشود")
    category = models.ForeignKey(Category_Weblog  ,related_name="post_weblog" , verbose_name="دسته بندی این پست" , on_delete=models.CASCADE , help_text="دسته بندی مرتبط به این پست را انتخاب کنید")
    tags     = models.ManyToManyField(Tags_Weblog , related_name="post_weblog" , verbose_name="تگ پست های وبسایت" , help_text="بیش از یکی هم میتوان انتخاب نمود")
    text = RichTextField(verbose_name="متن محتوای پست")
    creation = django_jalali_models.jDateTimeField(verbose_name="انتخاب زمان ساخت" , auto_now_add=False )
    time_duration = models.PositiveSmallIntegerField(verbose_name="زمان مورد نیاز برای مطالعه")
    author = models.ForeignKey(User , verbose_name="نویسنده" , on_delete=models.CASCADE , help_text="انتخاب نویسنده" , related_name="post_weblog")
    status = models.BooleanField(verbose_name="آیا منتشر شود ؟" , default=False , help_text="وضعیت انتشار خود را مشخص کنید    ")

    objects = Weblog_Manager()
    def __str__(self):
        return self.post_name


    def get_absolute_url(self):
        return reverse("weblog:Detail_Post" , args=[str(self.id) ] )

    class Meta :
        db_table = 'Post_Weblog'
        verbose_name_plural =  "وبلاگ وبسایت"


class Comments_Weblog(models.Model):
    post   = models.ForeignKey(Post_Weblog , verbose_name="انتخاب پست" , on_delete=models.CASCADE , help_text="پست مورد نظر را انتخاب کنید")
    person = models.ForeignKey(User , related_name="Comments_weblog" , verbose_name="انتخاب کاربر وبسایت" , on_delete=models.CASCADE , help_text="کاربر مدنظر که لاگین کرده است میتواند کامنت را ثبت کند")
    title  = models.CharField(verbose_name="عنوان کامنت" , max_length=100 )
    text  = models.TextField(verbose_name="متن کامنت ")


    def __str__(self):
        return self.title

    class Meta :
        db_table = 'Comments'
        verbose_name_plural = "کامنت پست ها"
        ordering = ["-id"]






