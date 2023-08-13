from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'blog-home'),
    path("page1.html/", views.page1, name = 'blog-page1'),
    path("page2.html/", views.page2, name = 'blog-page2'),
]