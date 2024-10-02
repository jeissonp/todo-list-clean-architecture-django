from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from ..use_cases.commands.create_task import CreateTaskCommand
from ..use_cases.queries.get_task_list import GetTaskListQuery
from ..interfaces.repository import TaskRepository

class TaskListView(APIView):
    def get(self, request):
        # Obtener todas las tareas
        task_repository = TaskRepository()
        query = GetTaskListQuery(task_repository)
        tasks = query.execute()

        # Serializar las tareas
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear una nueva tarea
        task_repository = TaskRepository()
        command = CreateTaskCommand(task_repository)

        title = request.data.get('title')
        description = request.data.get('description', '')

        # Serializador para la validación de datos
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Ejecutar el comando
                command.execute(title=title, description=description)
                return Response({"message": "Tarea creada con éxito"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)