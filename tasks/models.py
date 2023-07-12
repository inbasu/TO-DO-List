from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=128, blank=False, null=True)
    to_list = models.ForeignKey(to="List", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text)

    def done(self):
        self.is_done = not self.is_done
        self.save()


class List(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("list", kwargs={"list_name": self.pk})
