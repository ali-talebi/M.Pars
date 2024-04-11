from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User
from django.urls import reverse
# Create your models here.



class Category_Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name="دسته بندی محصولات")
    slug = models.SlugField(verbose_name="آدرس اینترنتی دسته بندی محصولات" , unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category_Product'
        verbose_name_plural = "دسته بندی محصولات"


class Tag_Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name="تگ محصولات")
    slug = models.SlugField(verbose_name="آدرس اینترنتی تگ محصولات" , unique=True )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Tag_Product'
        verbose_name_plural = "تگ های محصولات"


class Product_Product(models.Model):

    picture1 = models.FileField(upload_to='Product/%Y/%m/%d', verbose_name="تصویر1")
    picture2 = models.FileField(upload_to='Product/%Y/%m/%d', verbose_name='تصویر2')
    picture3 = models.FileField(upload_to='Product/%Y/%m/%d', verbose_name='تصویر3')
    picture4 = models.FileField(upload_to='Product/%Y/%m/%d', verbose_name="تصویر4")

    product_name = models.CharField(max_length=100 , verbose_name="نام محصول")
    slug         = models.SlugField(verbose_name= "آدرس اینترنتی محصول" , unique=True  , help_text="به طور خودکار این فیلد مقدار دهی میشود" )
    text = RichTextField(verbose_name="توضیحات")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="میزان قیمت محصول")
    category = models.ForeignKey(Category_Product , related_name='products' , on_delete=models.CASCADE , verbose_name="دسته بندی محصول")
    tags = models.ManyToManyField(Tag_Product , related_name='products' , verbose_name="تگ های محصولات")

    def get_absolute_url(self):
        return reverse('product:detail_product' , args=[str(self.id)])


    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'Product_Product'
        verbose_name_plural = "مشخصات محصولات"




class Comment_Product(models.Model):
    product = models.ForeignKey(Product_Product , on_delete=models.CASCADE , verbose_name="محصول" , related_name="comment_product" , help_text="محصول مورد نظر" )
    person  = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="فرد نظر دهنده" , related_name='comment_product' , help_text="")
    title   = models.CharField(max_length=100 , verbose_name="عنوان کامنت برای محصول")
    text = models.TextField(verbose_name="متن کامنت برای محصول" )

    def __str__(self) :
        return self.title

    class Meta:
        db_table = 'Comment_Product'
        verbose_name_plural = "کامنت برای محصولات"