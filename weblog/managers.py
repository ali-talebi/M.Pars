from django.db import models


class Weblog_Manager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=True)