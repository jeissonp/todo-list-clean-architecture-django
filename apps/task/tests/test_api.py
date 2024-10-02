from rest_framework.test import APITestCase
from rest_framework import status
from apps.task.infrastructure.models import TaskModel

class TestTaskAPI(APITestCase):

    def test_create_task_with_valid_data(self):
        # Hacer una solicitud POST para crear una tarea
        url = "/api/tasks/"
        data = {
            "title": "Nueva Tarea",
            "description": "Descripción de la tarea"
        }
        response = self.client.post(url, data, format='json')

        # Verificar que la tarea se haya creado correctamente
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TaskModel.objects.count(), 1)
        self.assertEqual(TaskModel.objects.first().title, "Nueva Tarea")

    def test_create_task_without_title_returns_error(self):
        url = "/api/tasks/"
        data = {
            "description": "Descripción sin título"
        }
        response = self.client.post(url, data, format='json')

        # Verificar que se devuelva un error de validación
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_get_task_list(self):
        # Crear tareas para probar el listado
        TaskModel.objects.create(title="Tarea 1", description="Primera tarea")
        TaskModel.objects.create(title="Tarea 2", description="Segunda tarea")

        url = "/api/tasks/"
        response = self.client.get(url)

        # Verificar que se devuelven las tareas correctamente
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Tarea 1")
        self.assertEqual(response.data[1]['title'], "Tarea 2")

if __name__ == '__main__':
    unittest.main()