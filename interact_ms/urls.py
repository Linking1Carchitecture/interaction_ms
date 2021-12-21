from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from interact_ms.views.assistant_view import AssistantList
from interact_ms.views.assistant_view import AssistantDetail
from interact_ms.views.message_view import MessageList
from interact_ms.views.message_view import MessageDetail

urlpatterns = [
    path('assistants/', AssistantList.as_view()),
    path('assistants/<int:pk>', AssistantDetail.as_view()),
    path('messages/', MessageList.as_view()),
    path('messages/<int:pk>', MessageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)