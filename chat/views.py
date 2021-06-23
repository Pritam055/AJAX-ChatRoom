from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from django.urls import reverse_lazy

from .forms import Form1
from .models import Room, Message
# Create your views here.
def home(request):
    if request.method=="POST":
        form = Form1(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name'].lower()
            username = form.cleaned_data['username']
            status = 0 
            if not Room.objects.filter(name__iexact=room_name).exists(): 
                Room.objects.create(name=room_name)
                status = 1
            return HttpResponseRedirect(reverse_lazy('chatroom',kwargs={'room':room_name, 'username':username})) 
    else:
        form = Form1()
    available_rooms = Room.objects.all().order_by('name')
    context = {
        'rooms':available_rooms,
        'form': form
    }
    return render(request, 'chat/home.html', context)

def get_chat_room(request, room,username):
    print(request.is_ajax())
    room_details = Room.objects.get(name=room) 
    context = {
        'room_details': room_details,
        'username':username,
        'room_name':room
    }
    return render(request, 'chat/chatroom.html', context)

def get_send_message(request):
    if request.method=="POST":
        username = request.POST.get('username')
        room_name = request.POST.get('room_name')
        message = request.POST.get('body')   
        if message.strip() == "":
            return JsonResponse({"status":"error"})
        else:
            Message.objects.create(user=username, room=room_name, body=message)
            return JsonResponse({"status":"success"})

def get_all_messages(request, room):  
    message_list = list(Message.objects.filter(room=room).values()) 
    return JsonResponse({'message_list': message_list})