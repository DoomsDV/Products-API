from django.db import models

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
