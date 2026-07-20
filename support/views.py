from django.shortcuts import render
import json
from django.http import JsonResponse
import time
from orders.models import Order
from support.agents import run_support_agent
from . models import Conversation, Message
from django.shortcuts import get_object_or_404


def chat(request, order_id):
  if request.method=='POST':
    data = json.loads(request.body)
    user_message = data.get('message')

  if not user_message:
    return JsonResponse({"error": "Empty message"}, status=400)
  order=get_object_or_404(Order, id=order_id, user=request.user)

  conversation, created = Conversation.objects.get_or_create(user=request.user, order=order)
  Message.objects.create(conversation=conversation, role="user", content=user_message)
  
  #Send user message and conversation to LLM
  reply= run_support_agent(user_message, conversation.id)
  
  #Store the LLM Reply
  Message.objects.create(conversation=conversation, role="agent", content=reply)

  return JsonResponse({"reply":"here is the reply"})
    
