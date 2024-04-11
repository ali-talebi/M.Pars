from django.contrib import admin
from .models import Category_Product , Tag_Product , Product_Product , Comment_Product
from django.utils.html import format_html

# Register your models here.



@admin.register(Category_Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' )

    search_fields = ('name' , )
    prepopulated_fields = {'slug' : ('name' , )}


@admin.register(Tag_Product)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' )
    search_fields = ('name' , )
    prepopulated_fields = {'slug' : ('name' , )  }


@admin.register(Product_Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name' , 'show_img' , 'slug' , 'price' , 'category' , 'show_tags' )

    prepopulated_fields = {'slug' : ('product_name' , )}
    def show_img(self , obj ) :
        return format_html('<img width=50px height=50px src="{}">'.format(obj.picture1.url))

    show_img.short_description = 'تصویر محصول'


    def show_tags(self , obj ) :
        return '|'.join([i.name for i in obj.tags.all()])

    show_tags.short_description = "تگ های محصول"


@admin.register(Comment_Product)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'product' , 'person' , 'title' , )

