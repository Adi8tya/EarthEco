from django.db import models

# Create your models here.

class Ecoproducts(models.Model):
    CATEGORY_CHOICES = [
        ('C', 'Cothing'),
        ('D', 'Daily Needs'),
        ('B', 'Bamboo Products'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


