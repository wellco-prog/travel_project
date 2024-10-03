# from django.db import models
#
# # Create your models here.
#
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('user', 'User')])
#
#     def __str__(self):
#         return self.name
#
# class Destination(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='destinations')
#
#     def __str__(self):
#         return self.name
