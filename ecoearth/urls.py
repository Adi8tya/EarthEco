from django.contrib import admin
from contact import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('', include('support.urls')),
]


