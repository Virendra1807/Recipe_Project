from django.db import models

class Student(models.Model):
    # id = models.AutoField()   
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True , blank=True)
    # image = models.ImageField()
    # file = models.FileField()


class Cars(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.name