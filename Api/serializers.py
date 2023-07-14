from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    class Meta:
        models = Todo
        fields = ['id','title','memo','created','datecompleted','important']
         