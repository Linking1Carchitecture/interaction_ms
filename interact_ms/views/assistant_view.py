from interact_ms.models.assistant_model import Assistant
from interact_ms.serializers.assistant_serializer import AssistantSerializer
from rest_framework import mixins
from rest_framework import generics

class AssistantList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print ("Respuesta del servidor", request)
        return self.create(request, *args, **kwargs)

class AssistantDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
