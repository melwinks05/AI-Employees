from django.contrib import admin
from . models import Message, Conversation, AgentLog

admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(AgentLog)
