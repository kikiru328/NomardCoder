from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_rooms(request):
    # get all the rooms
    rooms = Room.objects.all()

    # render template
    # render(request, template name)
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "Hello! this tile comes from Django!",
        },
    )


def see_one_room(request, room_id):
    return HttpResponse(f"see room with id: {room_id}")
