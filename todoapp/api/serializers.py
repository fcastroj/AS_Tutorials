
from rest_framework import serializers
from todo.models import Todo

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['completed']

class TodoSerializer(serializers.ModelSerializer):
 created = serializers.ReadOnlyField()
 completed = serializers.ReadOnlyField()
 class Meta:
    model = Todo
    fields = ['id', 'title', 'memo', 'created', 'completed']

class ToDoSerializer(serializers.ModelSerializer): 
 class Meta: 
   model = Todo 
   fields = ['title', 'memo', 'created', 'completed']