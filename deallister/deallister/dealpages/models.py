from django.db import models

# Create your models here.


class item(models.Model):
    item = models.CharField(max_length=20)
    price = models.IntegerField()
    origin = models.URLField()
    description = models.TextField()


    def __str__(self):
        return self.item
