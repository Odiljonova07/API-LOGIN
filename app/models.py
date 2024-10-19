from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE = [
        ("admin","admin"),
        ("xaridor","xaridor")
    ]
    image = models.ImageField(upload_to='user_image', null=True)
    phone_number = models.CharField(max_length=15)
    user_role = models.CharField(max_length=100, choices=USER_ROLE, default='xaridor')

    def __str__(self) -> str:
        return self.first_name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Watch(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='watch_imamge', null=True)
    cataegory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='watches')


    def __str__(self) -> str:
        return self.name

class Karzinka(models.Model):
    watch = models.OneToOneField(Watch, on_delete=models.CASCADE)
    numbers = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.watch.name

    
