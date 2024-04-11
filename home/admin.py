from django.contrib import admin
from .models import Slider
from django.utils.html import format_html
# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name' , 'show_img')

    def show_img(self, obj):
        return format_html('<img width=50px heigth=50px src="{}">'.format(obj.picture.url))
