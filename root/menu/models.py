from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # -->
    def __str__(self):
        return str(self.name)
    

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.FileField()
    price = models.FloatField()
    
    # --> 
    def __str__(self):
        return str(self.name)