from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def items(self):
        return Product.objects.filter(category=self).count()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(verbose_name="Description")
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
