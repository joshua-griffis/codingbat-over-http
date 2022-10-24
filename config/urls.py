from app.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('near-hundred/<int:n>/', near_hundred),
    path('string-splosion/<str:str>/', string_splosion),
    path('cat-dog/<str:str>/', cat_dog),
    path('lone-sum/<int:a>/<int:b>/<int:c>/', lone_sum),
    path('admin/', admin.site.urls),
]
