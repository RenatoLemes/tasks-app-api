from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

  task_owner = serializers.SerializerMethodField()

  def get_task_owner(self, obj):
    request = self.context['request']
    return request.user == obj.task_owner

  class Meta:
    model = Task
    fields = [
      'title', 'due_date', 'created_at', 'overdue', 'priority', 'task_owner'
    ]