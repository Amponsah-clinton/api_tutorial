from django.db import models

# Create your models here.

class items(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    