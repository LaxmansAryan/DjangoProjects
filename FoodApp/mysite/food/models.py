from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    username = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.melbournefoodandwine.com.au/image-tools.php?w=560&h=440&src=/recipes/recipe-placeholder.jpg")
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    