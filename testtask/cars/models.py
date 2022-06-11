from django.db import models


class CarCategories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cars(models.Model):
    carCategory = models.ForeignKey(CarCategories, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    company = models.CharField(max_length=20)
    makeYear = models.CharField(max_length=10)
    registrationNo = models.CharField(max_length=100)
    horsePower = models.CharField(max_length=20)

    def __str__(self):
        return self.model

