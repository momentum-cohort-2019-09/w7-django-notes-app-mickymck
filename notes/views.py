from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from notes.models import Note, Comment
from notes.forms import NewNoteForm, CommentForm
from notes.serializers import NoteSerializer, CommentSerializer


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def notes_list(request, format=None):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def notes_detail(request, pk, format=None):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        



# def notes_list(request):
#     all_notes = Note.objects.all()
#     return render(request, "notes/notes_list.html", {
#         "notes": all_notes,
#     })

    

# def notes_detail(request, pk):
#     note = Note.objects.get(pk=pk)
#     return render(request, "notes/notes_detail.html", {
#         "note": note,
#     })



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
        return redirect('/', pk=note.pk)



def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    new_body = request.POST.get('body')
    if new_body:
        note.body = new_body
        note.save()
        return redirect('/', pk=note.pk)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
