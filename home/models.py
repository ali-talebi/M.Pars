from django.db import models

# Create your models here.


class Slider(models.Model):
    name = models.CharField(verbose_name="عنوان اسلایدر" , max_length = 100 )
    picture = models.FileField(verbose_name="تصویر" , upload_to = f"Silder/{name}/")


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'slider'
        verbose_name_plural = "تصاویر اسلایدر"