from django.shortcuts import render
from notes.data import NOTES

# Create your views here.

def notes_list(request):
    return render(request, "notes/notes_list.html", {
        "notes": NOTES,
    })

def notes_detail(request, num):
    entry = NOTES[num]
    return render(request, "notes/notes_detail.html", {
        "entry": entry,  
    })
