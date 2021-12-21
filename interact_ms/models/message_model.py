from django.db import models
from .assistant_model import Assistant

class Message(models.Model):

    id_message = models.AutoField(primary_key = True)
    id_assistant = models.ForeignKey(Assistant, on_delete = models.CASCADE)
    body_message = models.CharField(max_length = 1500)
    hour_message = models.CharField(max_length = 5)

    class Meta:
        app_label = 'interact_ms'