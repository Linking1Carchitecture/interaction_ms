from rest_framework import serializers
from interact_ms.models.message_model import Message
from interact_ms.models.assistant_model import Assistant
from interact_ms.serializers.assistant_serializer import AssistantSerializer

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id_message', 'id_assistant', 'body_message', 'hour_message']

    def create(self, validated_data):

        message = Message(id_message = validated_data.get("id_message"),
                          id_assistant = validated_data.get("id_assistant"),
                          body_message = validated_data.get("body_message"),
                          hour_message = validated_data.get("hour_message"))
        message.save()
        return message

    def update(self, instance, validated_data):

        instance.id_message = validated_data.get("id_message")
        instance.id_assistant = validated_data.get("id_assistant")
        instance.body_message = validated_data.get("body_message")
        instance.hour_message = validated_data.get("hour_message")
        instance.save()
        return instance

    def to_representation(self, obj):

        data = super().to_representation(obj)

        assistant = Assistant.objects.get(id = data["assistant"])
        assistantSerializer = AssistantSerializer(assistant)

        data["assistant"] = assistantSerializer.data

        return data
