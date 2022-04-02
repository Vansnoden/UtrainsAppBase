from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.EmailField("Email", blank=True, unique=True)
    name = models.CharField("Name", blank=False, max_length=50)
    phone = models.CharField("Phone", blank=False, max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name