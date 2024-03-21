from django.shortcut import render, HttpResponse

def home(request):
    return HttpResponse("anjay mabar")