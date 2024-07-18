from django.urls import path
from django.contrib import admin
from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
]