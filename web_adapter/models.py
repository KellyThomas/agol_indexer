from __future__ import unicode_literals
from django.db import models


class Web_Adapter(models.Model):
    machine_name = models.CharField(max_length=20)
    # TODO: Fix typo in environment
    enviroment = models.CharField(max_length=20)
    alias = models.CharField(max_length=40)
    description = models.TextField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Web Adapter'
        ordering = ['machine_name']

    def __str__(self):
        return self.machine_name
