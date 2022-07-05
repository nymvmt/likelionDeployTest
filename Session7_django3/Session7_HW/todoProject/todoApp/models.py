from django.db import models

# Create your models here.

class Todo(models.Model):
    Todo_title = models.CharField(max_length=1000)
    Todo_detail = models.TextField(blank=True)
    Todo_due = models.DateField()
    def __str__(self):
        return self.Todo_title