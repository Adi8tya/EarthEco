from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    order_number = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=100, blank=False)
    content = models.TextField()
