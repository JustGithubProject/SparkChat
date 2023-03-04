from django.shortcuts import render


def chat_room(request, room_name):
    return render(request, "chat.html", {"room_name": room_name})


def main(request):
    room_link = request.GET.get("entry")
    return render(request, "main.html", {'room_link': room_link})