from django.test import TestCase

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from tasks.models import Task, List

User = get_user_model()


class TestTask(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        text = "Task test text"
        user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        to = List.objects.create(name="default name", owner=user)
        Task.objects.create(text=text, to_list=to)

    def test_creater_new_task(self):
        item = Task.objects.get(pk=1)
        self.assertEqual(1, Task.objects.count())
        self.assertEqual(item.text, "Task test text")

    def test_str_representation(self):
        item = Task.objects.get(pk=1)
        self.assertEqual(str(item), "Task test text")

    def test_task_is_done(self):
        item = Task.objects.get(pk=1)
        self.assertFalse(item.is_done)
        item.done()
        self.assertTrue(item.is_done)

    def test_create_new_task_with_no_text(self):
        with self.assertRaises(ValidationError):
            task = Task.objects.create(text="", to_list=List.objects.get(pk=1))
            task.full_clean()
            task.save()


class TestList(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        name = "First list"
        user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        List.objects.create(name=name, owner=user)

    def test_creater_new_list(self):
        item = List.objects.get(pk=1)
        self.assertEqual(1, List.objects.count())
        self.assertEqual(item.name, "First list")

    def test_str_representation(self):
        item = List.objects.get(pk=1)
        self.assertEqual(str(item), "First list")

    def test_create_new_list_with_no_name(self):
        with self.assertRaises(ValidationError):
            lst = List.objects.create(name="", owner=User.objects.get(pk=1))
            lst.full_clean()
            lst.save()

    def test_create_new_list_with_no_owner(self):
        with self.assertRaises(IntegrityError):
            lst = List.objects.create(name="Text name", owner=None)
            lst.full_clean()
            lst.save()

    def test_get_absolute_url(self):
        self.assertEqual(List.objects.get(pk=1).get_absolute_url(), "/1/list")
