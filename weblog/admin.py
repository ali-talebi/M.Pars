from django.contrib import admin
from .models import Post_Weblog , Category_Weblog , Comments_Weblog , Tags_Weblog
from django.utils.html import format_html
from django.contrib import messages
from django_jalali.admin.filters import JDateFieldListFilter
# Register your models here.


@admin.register(Tags_Weblog)
class Tags_WeblogAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug' )
    search_fields = ('tag_name', 'slug')
    prepopulated_fields = {'slug': ('tag_name',)}




@admin.register(Post_Weblog)
class Post_WeblogAdmin(admin.ModelAdmin):
    list_display = ('post_name' , 'show_img' , 'slug'  , 'category' , 'show_tags' , 'show_creation' , 'author' , 'status'  )
    search_fields = ('post_name' , 'slug' , 'category' , 'author' )
    list_filter = (
        ('creation', JDateFieldListFilter),
        ('status' ) ,
    )
    prepopulated_fields = {'slug': ('post_name','category' , )}


    def show_creation(self , obj ) :
        return obj.creation.strftime('%H:%M _ %Y/%m/%d')

    show_creation.short_description = 'زمان ایجاد '
    def show_tags(self , obj ):
        return '|'.join([i.tag_name for i in obj.tags.all()])
    show_tags.short_description = 'تگ های مقالات'

    def show_img(self , obj ):
        return format_html('<img width=50px heigth=50px src="{}">'.format(obj.picture.url))

    show_img.short_description = 'عکس پست وبلاگ'
    def Activate_Status(self, request, queryset) :
        queryset.update(status = True )
        messages.info(request, 'وضعیت به منتشر شده تغییر پیدا کرد')

    Activate_Status.short_description = 'تبدیل وضعیت به منتشر شده'



    def Deactivate_Status(self, request, queryset) :
        queryset.update(status = False )
        messages.info(request,'وضعیت به پیش نویس تغییر پیدا کرد')

    Deactivate_Status.short_description = 'تبدیل به عدم انتشار پست'



    actions = [Activate_Status , Deactivate_Status]

@admin.register(Category_Weblog)
class Category_WeblogAdmin(admin.ModelAdmin):
    list_display = ('category_name' , 'slug' )
    search_fields = ('category_name' , )
    prepopulated_fields = {'slug': ('category_name', )}


@admin.register(Comments_Weblog)
class Comments_WeblogAdmin(admin.ModelAdmin):
    list_display = ('post' , 'person' , 'title' , 'text' )
    search_fields = ('person' , 'title' , )

