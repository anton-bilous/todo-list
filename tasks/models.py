from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")


class Tag(models.Model):
    name = models.CharField(max_length=255)
