from django.db import models

class Assistant(models.Model):

    id_assistant = models.AutoField(primary_key = True)
    name_assistant = models.CharField(max_length = 20)
    raise_hand_assistant = models.CharField(max_length=20)

    class Meta:
        app_label = 'interact_ms'
