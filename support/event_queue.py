import queue

subscribers = {}

def subscribe(coneversation_id):
  q = queue.Queue()  # creates new queue

  if coneversation_id not in subscribers:
    subscribers[coneversation_id] = []

  subscribers[coneversation_id].append(q)
  return q

def unsubscribe(conversation_id, q):
  if conversation_id in subscribers:
    subscribers[conversation_id].remove(q)
    if not subscribers[conversation_id]:
      del subscribers[conversation_id]

def publish(conversation_id, event):
  if conversation_id in subscribers:
    for q in subscribers[conversation_id]:
      q.put(event)


# sentinal value to stop streaming
DONE = {"type":"done"}