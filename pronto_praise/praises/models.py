from django.db import models


class Praise(models.Model):
    to = models.CharField(max_length=500, blank=False, null=False)
    by = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    number_of_hearts = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
