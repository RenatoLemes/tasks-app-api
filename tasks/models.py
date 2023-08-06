from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
  HIGH = 'High'
  MEDIUM = 'Medium'
  LOW = 'Low'
  PRIORITY_CHOICES = [
    (HIGH, 'High'),
    (MEDIUM, 'Medium'),
    (LOW, 'Low')
  ]
  title = models.CharField(max_length=100)
  due_date = models.DateField()
  created_at = models.DateTimeField(default=timezone.now, blank=True)
  overdue = models.BooleanField(default=False)
  task_owner = models.ForeignKey(User, on_delete=models.CASCADE)
  priority = models.CharField(
    max_length=6,
    choices=PRIORITY_CHOICES,
    default=MEDIUM
  )
  state = models.CharField(max_length = 15)
  
# this will show the task which will be expired first
  class Meta:
    ordering = ['-due_date']

  def __str__(self):
        return f'{self.id} {self.title}'

  
