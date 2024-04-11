# Generated by Django 4.2.11 on 2024-04-03 15:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category_Weblog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(max_length=100, verbose_name="نام دسته بندی "),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="این فیلد به طوری خودکار مقدار دهی میشود",
                        unique=True,
                        verbose_name="آدرس اینترنتی دسته بندی",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "دسته بندی پست های وبلاگ",
                "db_table": "Category_Weblog",
            },
        ),
        migrations.CreateModel(
            name="Post_Weblog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "picture",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="Post_Weblog/%Y/%m/%d",
                        verbose_name="عکس مورد نظر",
                    ),
                ),
                (
                    "post_name",
                    models.CharField(max_length=100, verbose_name="عنوان پست ها"),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="به طور خودکار مقدار دهی میشود",
                        verbose_name="آدرس اینترنتی پست",
                    ),
                ),
                ("text", ckeditor.fields.RichTextField(verbose_name="متن محتوای پست")),
                ("creation", models.DateTimeField(verbose_name="انتخاب زمان ساخت")),
                (
                    "time_duration",
                    models.PositiveSmallIntegerField(
                        verbose_name="زمان مورد نیاز برای مطالعه"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=False,
                        help_text="وضعیت انتشار خود را مشخص کنید    ",
                        verbose_name="آیا منتشر شود ؟",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="انتخاب نویسنده",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_weblog",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="نویسنده",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="دسته بندی مرتبط به این پست را انتخاب کنید",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_weblog",
                        to="weblog.category_weblog",
                        verbose_name="دسته بندی این پست",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "وبلاگ وبسایت",
                "db_table": "Post_Weblog",
            },
        ),
    ]
