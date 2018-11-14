from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    origin = models.URLField()
    description = models.TextField()


    def __str__(self):
        return self.item_name
