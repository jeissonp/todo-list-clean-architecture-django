class Task:
    def __init__(self, title, description='', completed=False):
        # Validaciones de dominio
        if not title:
            raise ValueError("El título no puede estar vacío.")
        if len(title) > 255:
            raise ValueError("El título no puede tener más de 255 caracteres.")

        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False