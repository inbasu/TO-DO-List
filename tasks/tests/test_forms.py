from django.test import TestCase
from tasks.forms import TaskForm, ListForm


class TaskFormTest(TestCase):
    def test_placeholder_in_form(self):
        form = TaskForm()
        self.assertIn('placeholder="Write a new task text"', form.as_p())

    def test_form_validation(self):
        form = TaskForm(data={"text": ""})
        self.assertFalse(form.is_valid())


class ListFormTest(TestCase):
    def test_placeholder_in_form(self):
        form = ListForm()
        self.assertIn('placeholder="New list name"', form.as_p())

    def test_form_validation(self):
        form = ListForm(data={"text": ""})
        self.assertFalse(form.is_valid())
