from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

 path('article/',article_list),
 path('detail/<int:id>/',article_detail),
 path('delete/<int:id>/',)


]