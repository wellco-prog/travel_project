from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICE = [('male', 'male'),
                     ('female', 'female')]
    username = models.CharField('Никнейм',max_length=50,unique=True)
    email = models.EmailField('Почта', max_length = 50,unique=True)
    avatar = models.ImageField('Аватарка', upload_to='users/', blank=True, null=True)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    gender = models.CharField('Пол', choices=GENDER_CHOICE, default='male')
    about = models.TextField('О себе', blank=True, null=True)
    # fav_movies = models.ManyToManyField('film.Film', related_name='favorite_film')
    # friend = models.ManyToManyField('self')
    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользователи'