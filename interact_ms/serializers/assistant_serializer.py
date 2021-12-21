from rest_framework import serializers

from interact_ms.models.assistant_model import Assistant

class AssistantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assistant
        fields = ['id_assistant', 'name_assistant', 'raise_hand_assistant']
