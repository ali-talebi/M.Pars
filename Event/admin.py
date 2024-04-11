from django.contrib import admin
from .models import Event_Information , Event_Comment
from django.utils.html import format_html
# Register your models here.


@admin.register(Event_Information)
class Event_InformationAdmin(admin.ModelAdmin):
    list_display = ('event_name' , 'show_img' , 'location' , 'show_time' , 'price'  )
    search_fields = ['event_name' , 'location'  ]


    def show_img(self, obj):
        return format_html('<img width=50px heigth=50px src="{}">'.format(obj.picture.url))

    def show_time(self , obj ) :
        return obj.time.strftime('%H:%M _ %Y/%m/%d')



@admin.register(Event_Comment)
class Event_CommentAdmin(admin.ModelAdmin) :
    list_display = ('event' , 'title'  , 'text' )
    search_fields = ['event' , 'title' ]