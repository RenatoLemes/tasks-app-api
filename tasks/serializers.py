from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
  # owner = serializers.ReadOnlyField(source='owner.username')
  task_owner = serializers.SerializerMethodField()

  def get_task_owner(self, obj):
    request = self.context['request']
    return request.user == obj.task_owner

  class Meta:
    model = Task
    fields = [
      'title', 'due_date', 'created_at', 'overdue', 'priority', 'task_owner'
    ]

class TaskDetailSerializer(TaskSerializer):

    tasks = serializers.ReadOnlyField(source='tasks.id')


# from rest_framework import serializers
# from .models import Task

# class TaskSerializer(serializers.ModelSerializer):

#   task_owner = serializers.ReadOnlyField(source='task_owner.username')

#   def create(self, validated_data):
#     validated_data['task_owner'] = self.context['request'].user
#     return super(TaskSerializer, self).create(validated_data)

#   # def get_task_owner(self, obj):
#   #   request = self.context['request']
#   #   return request.user == obj.owner

#   class Meta:
#     model = Task
#     fields = [
#       'title', 'due_date', 'created_at', 'overdue', 'priority', 'task_owner'
#     ]