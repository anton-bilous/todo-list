from django.urls import path

from .views import TaskListView, TaskUpdateView


app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]
