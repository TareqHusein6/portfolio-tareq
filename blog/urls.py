from django.urls import path
#get views from portfolio
from . import views

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
]

