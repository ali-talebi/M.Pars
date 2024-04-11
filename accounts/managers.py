from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):


    def create_user(self , phone_number , email , full_name ,password  ) :
        if not phone_number :
            raise ValueError('َشماره تلفن اجباری میباشد')

        if not email:
            raise ValueError('ایمیل اجباری میباشد')

        if not full_name :
            raise ValueError('نام و نام خانوادگی اجباری میباشد')

        user = self.model(phone_number = phone_number , email = self.normalize_email(email) ,full_name =full_name , password =password )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self , phone_number , email , full_name ,password ) :
        user = self.create_user(phone_number = phone_number , email = self.normalize_email(email) , full_name = full_name , password=password)
        user.is_admin = True

        user.save(using=self._db)
        return user
