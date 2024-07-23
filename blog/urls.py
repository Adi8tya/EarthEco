from django.contrib import admin
from django.urls import path,include
from . import views
from .views import Blogs, HomeView, ArticleDetailView, AddPostView, UpdatePostView,DeletePostView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',views.home,name='home'),
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='article-edit'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='article-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

