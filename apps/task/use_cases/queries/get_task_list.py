class GetTaskListQuery:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self):
        # Obtener todas las tareas del repositorio
        return self.task_repository.get_all()