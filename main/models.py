from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    title = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )

    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True, upload_to='products')
    price = models.IntegerField()
    status = models.CharField(choices=CHOICES, max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

