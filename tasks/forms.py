from django.forms import ModelForm


from tasks.models import Task


class TaskForm(ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = Task
        fields = ["text"]
