from rest_framework import serializers
from .models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['id', 'title', 'description', 'completed']

    # Validación a nivel de campo
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("El título es obligatorio.")
        if len(value) > 255:
            raise serializers.ValidationError("El título no puede tener más de 255 caracteres.")
        return value

    # Validación a nivel de objeto
    def validate(self, data):
        # Evitar KeyError utilizando get para 'completed'
        if data.get('completed', False) and not data.get('title', ''):
            raise serializers.ValidationError("No puedes completar una tarea sin título.")
        return data