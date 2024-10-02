from ...domain.task import Task

class CreateTaskCommand:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, title, description=''):
        try:
            # Crear una nueva tarea, las validaciones ocurren aquí
            task = Task(title=title, description=description)
            # Guardar la tarea usando el repositorio
            self.task_repository.save(task)
        except ValueError as e:
            # Lanzar una excepción para el controlador que maneja la API
            raise Exception(f"Error en la creación de la tarea: {str(e)}")