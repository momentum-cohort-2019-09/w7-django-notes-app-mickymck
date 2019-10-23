from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import NewNoteForm

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

def new_note(request):
    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            newNote = form.save()
            return redirect ('/')
    else:
        form = NewNoteForm()

    return render(request, "notes/create_new_note.html", {"form": form})

        