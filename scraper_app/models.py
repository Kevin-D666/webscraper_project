from django.db import models

# Create your models here.
view = models


class Search(models.Model):
    search_field = models.CharField(max_length=255)
