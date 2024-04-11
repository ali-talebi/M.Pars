from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import Group
from .models import User , otpCode , Team_Member , Skills
# Register your models here.


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name' , )



@admin.register(Team_Member)
class Team_MemberAdmin(admin.ModelAdmin):
    list_display = ( 'give_fulll_name' , 'introduce'   )

@admin.register(otpCode)
class otpCode_Admin(admin.ModelAdmin):
    list_display = ('phone_number' , 'code' , 'creation')





class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email' , 'full_name' , 'is_active' , 'is_staff' )
    list_filter = ['is_admin' , ]


    fieldsets = (
        ('مشخصات کاربران' , {'fields': ('email', 'phone_number' , 'full_name' , 'password' , 'picture' )}) ,
        ('دسترسی ها' , {'fields': ('is_active', 'is_admin'  , 'last_login') }  )
    )

    add_fieldsets = (
        ('ساخت  کاربران جدید' , {'fields': ('email', 'phone_number' , 'full_name' , 'picture' , 'password1' , 'password2')}) ,
    )



    search_fields = ['email' , 'full_name']

    ordering = ('email' , 'full_name')



    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User , UserAdmin)