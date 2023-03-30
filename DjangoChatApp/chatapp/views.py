from django.shortcuts import render
from chatapp.models import ChatRoom, ChatMessages


# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()

    return render(request, 'chatapp/index.html', {'chatrooms':chatrooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessages.objects.filter(room=chatroom)[0:30]
    return render(request, 'chatapp/room.html',{'chatroom': chatroom, 'messages': messages})
