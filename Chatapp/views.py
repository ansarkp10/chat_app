from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.urls import reverse
from .models import Room, Message
from django.conf import settings

def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        avatar = request.FILES.get('avatar')  # Handle the uploaded image

        # Save the avatar file
        avatar_url = None
        if avatar:
            avatar_path = default_storage.save(f'avatars/{avatar.name}', avatar)
            avatar_url = avatar_path  # Store the relative path

        # Check if the room already exists or create a new one
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()

        # Redirect to the room view with avatar as a query parameter
        room_url = reverse('room', kwargs={'room_name': room, 'username': username})
        return redirect(f'{room_url}?avatar={avatar_url}')

    return render(request, 'index.html')

def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    avatar_url = request.GET.get('avatar', None)  # Retrieve the avatar from the URL query parameters

    # Prepend MEDIA_URL if the avatar_url is valid
    if avatar_url:
        avatar_url = f'{settings.MEDIA_URL}{avatar_url}'

    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
        "avatar_url": avatar_url,  # Pass the avatar to the template
    }

    return render(request, 'message.html', context)
