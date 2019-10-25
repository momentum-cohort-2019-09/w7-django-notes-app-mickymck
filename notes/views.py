from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NewNoteForm, CommentForm

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



def add_comment(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.note = note
            comment.save()
            return redirect(to='notes_list')
    else:
        form = CommentForm()

    return render(request, "notes/comment.html", {"form": form})  



def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect(to='notes_list')
    return render(request, 'notes/note_delete.html', {"note": note})



def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    new_body = request.POST.get('body')
    if new_body:
        note.body = new_body
        note.save()
        return redirect('/', pk=note.pk)
