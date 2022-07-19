from django.db import models


class PopularPostManager(models.Manager):
    def get_queryset(self):
        return super(PopularPostManager, self).get_queryset().filter(is_popular=True)


class TopAuhtorManager(models.Manager):
    def get_queryset(self):
        return super(TopAuhtorManager, self).get_queryset().filter(is_top=True)

