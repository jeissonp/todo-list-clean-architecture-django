import unittest
from apps.task.domain.task import Task

class TestTaskDomain(unittest.TestCase):

    def test_create_task_with_valid_title(self):
        task = Task(title="Tarea válida", description="Una descripción")
        self.assertEqual(task.title, "Tarea válida")
        self.assertEqual(task.description, "Una descripción")
        self.assertFalse(task.completed)

    def test_create_task_without_title_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            Task(title="")

        self.assertEqual(str(context.exception), "El título no puede estar vacío.")

    def test_create_task_with_long_title_raises_exception(self):
        long_title = "A" * 256  # Más de 255 caracteres
        with self.assertRaises(ValueError) as context:
            Task(title=long_title)

        self.assertEqual(str(context.exception), "El título no puede tener más de 255 caracteres.")

    def test_mark_task_completed(self):
        task = Task(title="Tarea válida")
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_mark_task_incomplete(self):
        task = Task(title="Tarea válida", completed=True)
        task.mark_incomplete()
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()