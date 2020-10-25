from django.urls import path
#get views from portfolio
from . import views

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:post_id>/', views.detail, name="detail"),#if anyone enters an integer after blog url, then pass the int as blog_id to views_detail
]

