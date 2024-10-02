from unittest import TestCase
from unittest.mock import MagicMock
from apps.task.interfaces.repository import TaskRepository
from apps.task.infrastructure.models import TaskModel

class TestTaskRepository(TestCase):
    def setUp(self):
        self.repository = TaskRepository()

    def test_get_all_tasks(self):
        # Mockear la query a la base de datos
        TaskModel.objects.all = MagicMock(return_value=["Tarea1", "Tarea2"])
        tasks = self.repository.get_all()
        self.assertEqual(tasks, ["Tarea1", "Tarea2"])

    def test_get_task_by_id(self):
        # Mockear el método get de TaskModel
        TaskModel.objects.get = MagicMock(return_value="Tarea encontrada")
        task = self.repository.get_by_id(1)
        self.assertEqual(task, "Tarea encontrada")

    def test_save_task(self):
        # Mockear el método save
        task_mock = MagicMock()
        TaskModel.save = MagicMock()

        task = task_mock(title="Nueva Tarea", description="Descripción")
        self.repository.save(task)

        # Asegurarse de que el método save haya sido llamado
        TaskModel.save.assert_called_once()

if __name__ == '__main__':
    unittest.main()