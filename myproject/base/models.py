from django.db import models

#[Person.objects.create(first_name=f"name#{i}" , last_name=f"prenon#{i}") for i in range(50)]
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)