from django.contrib import admin
from .models import Course_Information , Course_Category , Course_Tag
# Register your models here.



@admin.register(Course_Tag)
class Course_TagAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course_Category)
class Course_CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course_Information)
class Course_InformationAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category', 'teacher' , 'level'  )
    search_fields = ('course_name', 'teacher', 'level')
