from profile import Profile

from django.db import models

# Create your models here.
from account.models import User


















class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='users')


    def __str__(self):
        return self.first_name




class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False

class Products(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )
    title = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='products')
    image = models.ImageField(upload_to='products, blank=True, null=true')
    price = models.IntegerField()
    status = models.CharField(choices=CHOICES, max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_category(self):
        return self.category

    @property
    def get_image(self):
        return self.images.first()


class Image(models.Model):
    image = models.ImageField(upload_to='productes')
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')

    def str(self):
        return self.image.url



#     @property
#     def get_image(self):
#         return self.image.first()
#
#
#     # def get_absolute_url(self):
#     #     from django.urls import reverse
#     #     return reverse('detail', kwargs={'pk': self.pk})
#
# class Image(models.Model):
#     image =  models.ImageField(upload_to='productes')
#     recipe = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')








