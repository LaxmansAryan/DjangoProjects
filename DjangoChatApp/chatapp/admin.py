from django.contrib import admin
from chatapp.models import ChatRoom, ChatMessages

# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(ChatMessages)