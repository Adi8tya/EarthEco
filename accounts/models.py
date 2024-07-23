from django.db import models
from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'
# Create your models here.
