from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='blogs/profile/' , null=True, blank=True)
    fb = models.CharField(max_length=100, null=True,blank=True)
    twitter = models.CharField(max_length=100, null=True,blank=True)
    insta = models.CharField(max_length=100, null=True,blank=True)
    snap = models.CharField(max_length=100, null=True,blank=True)


    def __str__(self):
        return str(self.user)

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='blogs/', blank=True , null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id),))
# Create your models here.
