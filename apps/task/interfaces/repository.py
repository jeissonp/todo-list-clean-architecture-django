from ..infrastructure.models import TaskModel

class TaskRepository:
    def get_all(self):
        return TaskModel.objects.all()

    def get_by_id(self, task_id):
        return TaskModel.objects.get(id=task_id)

    def save(self, task):
        task_model = TaskModel(
            title=task.title,
            description=task.description,
            completed=task.completed
        )
        task_model.save()

    def delete(self, task_id):
        TaskModel.objects.filter(id=task_id).delete()