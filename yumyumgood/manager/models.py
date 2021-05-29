from django.db import models
from django.contrib.auth.models import User
from django.db.models import manager

class Profile(models.Model):
    ROLE_CHOICES = (
        ('M', 'manager'),
        ('H', 'head'),
        ('C', 'customer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    Cafeteria = models.ForeignKey("Cafeteria", on_delete=models.CASCADE, null = True)


class Cafeteria(models.Model):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return '{}'.format(self.name)

class Menu(models.Model):
    MEAL_CHOICES = (
        ('조식', '조식'),
        ('중식', '중식'),
        ('석식', '석식'),
    )

    STATUS_CHOICES = (
        ('판매 가능', '판매 가능'),
        ('판매 중지', '판매 중지'),
    )

    name = models.CharField(max_length=20)
    meal = models.CharField(max_length=2, choices=MEAL_CHOICES)
    sale_start_time = models.TimeField()
    sale_end_time = models.TimeField()
    sale_date = models.DateField()
    quantity = models.PositiveIntegerField(null=True)
    foods = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="판매 가능", null=True)
    cafeteria = models.ForeignKey("Cafeteria", on_delete=models.CASCADE)

    def getPk(self) :
        return self.id

    def __str__(self):
        return '{}'.format(self.name)

