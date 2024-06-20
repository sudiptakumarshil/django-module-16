from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=150)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now=False, auto_now_add=False)
    category = models.ManyToManyField(Category)