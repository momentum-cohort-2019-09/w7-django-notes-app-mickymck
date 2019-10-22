from django.shortcuts import render
from notes.data import NOTES
from notes.models import Note

# Create your views here.

def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": all_notes,
    })

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_detail.html", {
        "note": note,
    })
