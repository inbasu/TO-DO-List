from django.test import TestCase, Client
from django.contrib.auth import get_user_model


# Create your tests here.
class UserBaseTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()

    def test_login_url(self):
        resp = self.client.get("/user/login/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "users/templates/login.html")

    def test_regestration_url(self):
        resp = self.client.get("/user/registration/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "users/templates/registration.html")

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test_user", email="exemple@mail.te", password="superPassword"
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_logut_url(self):
        resp = self.client.get("/user/logout/")
        self.assertEqual(resp.status_code, 302)
