from .models import Task
from .forms import TaskForm


class TaskMixin:
    model = Task
    context_object_name = "tasks"
    paginate_by = 10


class TaskEditMixin:
    form_class = TaskForm
