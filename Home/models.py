from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ServiceRequest(models.Model):
    SERVICE_CATEGORIES = [
        ('C', 'Consultation'),
        ('W', 'Waste Management'),
        ('E', 'Energy Solutions'),
        ('P', 'Pollution Control'),
        ('O', 'Other')
    ]

    URGENCY_LEVELS = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]

    service_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=1, choices=SERVICE_CATEGORIES)
    urgency = models.CharField(max_length=1, choices=URGENCY_LEVELS)
    max_budget = models.IntegerField()

    def __str__(self):
        return self.service_name


class TeamApplication(models.Model):
    POSITION_CHOICES = [
        ('EV', 'Environmental Volunteer'),
        ('CT', 'Conservation Technician'),
        ('EM', 'Environmental Manager'),
        ('RS', 'Research Scientist'),
        ('EA', 'Environmental Activist'),
        ('O', 'Other')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"




class WhyEcoEarth(models.Model):
    REASON_CHOICES = [
        ('C', 'Conservation'),
        ('E', 'Education'),
        ('S', 'Sustainability'),
        ('A', 'Advocacy'),
        ('R', 'Research'),
        ('W', 'Waste Reduction'),
        ('B', 'Biodiversity'),
        ('M', 'Mitigation of Climate Change'),
        ('P', 'Public Awareness'),
        ('O', 'Other')
    ]
    title = models.CharField(max_length=200)
    reason = models.CharField(max_length=1, choices=REASON_CHOICES, default='C')
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




