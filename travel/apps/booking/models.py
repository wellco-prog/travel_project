from django.db import models
from django.utils.timezone import now


# Create your models here.
class Destination(models.Model):
    name = models.CharField('Направление', max_length=100)
    image = models.ImageField('Изображение', upload_to='static/image/',
                              blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Package(models.Model):
    naming = models.CharField('Название', max_length=100)
    destination = models.ForeignKey(Destination, verbose_name='Направление', on_delete=models.CASCADE)
    # author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    image = models.ImageField('Изображение', upload_to='static/image/',
                              blank=True, null=True)
    daysCount = models.IntegerField('Дней отдыха')
    personsCount = models.IntegerField('Количество Человек')
    price = models.IntegerField('Цена')
    offer = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.naming




class  Order(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    from_date = models.DateField('from_date', null=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package.naming
