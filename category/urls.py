from django.urls import path
from .views import add_category

urlpatterns = [
    path('add/', add_category,name='category.add'),
]