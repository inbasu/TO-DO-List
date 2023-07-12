from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from tasks.models import List, Task
from tasks.forms import TaskForm

# Create your views here.


class HomeView(LoginRequiredMixin, View):
    template = "tasks/templates/home.html"
    context = {"title": "Home"}

    def get(self, request):
        self.context["lists"] = List.objects.filter(owner=request.user)
        return render(request, template_name=self.template, context=self.context)

    def post(self, request):
        new_list = List.objects.create(
            name=request.POST["name"],
            owner=request.user,
        )
        new_list.save()
        return redirect(new_list)


class TaskListView(LoginRequiredMixin, View):
    template = "tasks/templates/list.html"
    context = {}

    def get(self, request, list_name):
        self.context["list"] = List.objects.get(pk=list_name)
        self.context["tasks"] = Task.objects.filter(to_list=self.context["list"])
        return render(request, template_name=self.template, context=self.context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task

    def post(self, request, list_name):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.to_list = List.objects.get(pk=list_name, owner=request.user)
            task.save()
        return redirect(task.to_list)


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    success_url = "/"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/"


@login_required
def done_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done()
    return redirect(task.to_list)
