from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100, unique=True)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField('Название тэга', max_length=100, unique=True)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')
    text2 = models.TextField('Текст2', blank=True, null=True)
    text3 = models.TextField('Текст3', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='Теги', related_name='posts')
    image = models.ImageField('Изображение', upload_to='images/',
                              blank=True, null=True)
    image2 = models.ImageField('Изображение2', upload_to='images/',
                               blank=True, null=True)
    image3 = models.ImageField('Изображение3', upload_to='images/',
                               blank=True, null=True)
    is_active = models.BooleanField('Активно', default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'