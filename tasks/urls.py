from django.urls import path

from tasks.views import (
    HomeView,
    TaskListView,
    TaskCreateView,
    TaskDeleteView,
    ListDeleteView,
    done_task,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:list_name>/list", TaskListView.as_view(), name="list"),
    path("del_list/<int:pk>", ListDeleteView.as_view(), name="del_list"),
    path("<int:list_name>/new", TaskCreateView.as_view(), name="new"),
    path("del_task/<int:pk>", TaskDeleteView.as_view(), name="del_task"),
    path("done_task/<int:pk>", done_task, name="done_task"),
]
