from django.forms import ModelForm, TextInput


from tasks.models import Task, List


class TaskForm(ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = Task
        fields = ["text"]

        widgets = {
            "text": TextInput(attrs={"placeholder": "Write a new task text"}),
        }


class ListForm(ModelForm):
    """Form definition for List."""

    class Meta:
        """Meta definition for Listform."""

        model = List
        fields = ("name",)

        widgets = {"name": TextInput(attrs={"placeholder": "New list name"})}
