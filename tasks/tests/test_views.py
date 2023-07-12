from django.test import TestCase, Client
from tasks.models import List, Task
from django.contrib.auth import get_user_model


User = get_user_model()


class TestHomeView(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        List.objects.create(name="base list", owner=cls.user)

    def setUp(self):
        self.client.force_login(self.user)
        self.path = "tasks/templates/home.html"
        self.url = "/"

    def test_view_have_url(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, self.path)

    def test_html_is_correct(self):
        resp = self.client.get(self.url)
        self.assertContains(resp, "base list")

    def test_delete_list(self):
        name_for_delete = "delete this list"
        lst = List.objects.create(name=name_for_delete, owner=User.objects.get(pk=1))
        self.assertEqual(2, List.objects.count())
        self.client.post(f"/del_list/{lst.pk}")
        self.assertEqual(1, List.objects.count())


class TestListView(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        to = List.objects.create(name="base list", owner=cls.user)
        for s in ["first", "second", "third"]:
            Task.objects.create(text=s, to_list=to)

    def setUp(self):
        self.client.force_login(self.user)
        self.path = "tasks/templates/list.html"
        self.url = "/1/list"

    def test_view_have_url(self):
        resp = self.client.get(self.url)
        self.assertTemplateUsed(resp, self.path)

    def test_html_is_correct(self):
        resp = self.client.get(self.url)
        self.assertContains(resp, "second")


class TestManageTasks(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        List.objects.create(name="test", owner=cls.user)

    def setUp(self):
        self.client.force_login(self.user)

    def test_create_new_task(self):
        text = "test to create new task"
        self.client.post("/1/new", {"text": text, "to_list": List.objects.get(pk=1)})
        item = Task.objects.last()
        self.assertEqual(str(item), text)

    def test_delete_task_with_post(self):
        text_for_delete = "delete it"
        Task.objects.create(text=text_for_delete, to_list=List.objects.get(pk=1))
        self.assertEqual(1, Task.objects.count())
        self.client.post("/del_task/1")
        self.assertEqual(0, Task.objects.count())

    def test_task_is_done_post(self):
        task = Task.objects.create(text="text for done", to_list=List.objects.get(pk=1))
        self.assertFalse(task.is_done)
        self.client.get(f"/done_task/{task.pk}")
        self.assertTrue(Task.objects.last().is_done)
