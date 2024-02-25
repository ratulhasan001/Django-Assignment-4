from django.db import models
from category.models import Category

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length = 50)
    task_description = models.TextField(blank = False)
    is_completed = models.BooleanField(default = False)
    category = models.ManyToManyField(Category)
    task_assign_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title