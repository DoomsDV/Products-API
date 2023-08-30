from django.db import models
import random
import string

class TimeLine(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sub_category(TimeLine):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'sub categorias'
        verbose_name_plural = 'sub categorías'

    def __str__(self):
        return self.name

class Category(TimeLine):
    name = models.CharField(max_length=50)
    sub_categories = models.ManyToManyField(Sub_category, blank=True)
    
    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
    
    def __str__(self):
        return self.name

class Brand(TimeLine):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
    
    def __str__(self):
        return self.name

class Product(TimeLine):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    price = models.PositiveBigIntegerField(default=0)
    url_image = models.URLField()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def generate_random_code(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_random_code()
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
