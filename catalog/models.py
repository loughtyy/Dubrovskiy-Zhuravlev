from django.db import models
from django.urls import reverse

class MyModelName (models.Model):
    my_field_name = models.CharField(max_length=20,help_text="Не более 20 символов")

class Meta:
    ordering = ["-my_field_name"]


def get_absolute_url(self):
    return reverse('model-detail-view', args=[str(self.id)])

def __str__(self):
    return self.field_name