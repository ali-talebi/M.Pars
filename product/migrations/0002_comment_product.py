# Generated by Django 4.2.11 on 2024-04-07 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment_Product",
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
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="عنوان کامنت برای محصول"
                    ),
                ),
                ("text", models.TextField(verbose_name="متن کامنت برای محصول")),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_product",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="فرد نظر دهنده",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="محصول مورد نظر",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_product",
                        to="product.product_product",
                        verbose_name="محصول",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "کامنت برای محصولات",
                "db_table": "Comment_Product",
            },
        ),
    ]
