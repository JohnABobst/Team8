from django.shortcuts import render

# Create your views here.
def event_detail(request,id):
    event = Event.objects.get(id=id)
    context = {
        'event': event
    }
    return render(request, 'event_detail.html', context)

def events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events.html', context)


