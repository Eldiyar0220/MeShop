from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories, blank=True, null=true')


    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=250)
    Opisanii = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='names')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='names')
    # user = models.TextField(Profile,related_name='recipes')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image =  models.ImageField(upload_to='recipes')
    recipe = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')

