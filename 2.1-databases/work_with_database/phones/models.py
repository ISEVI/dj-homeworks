from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(u'Название', max_length=64)
    price = models.IntegerField(u'Цена')
    image = models.TextField(u'Изображение')
    release_date = models.DateField(u'Дата публикации')
    lte_exists = models.BooleanField(max_length=64)
    slug = models.SlugField(max_length=64)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.name
