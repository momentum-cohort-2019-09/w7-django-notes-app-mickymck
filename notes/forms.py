from django.forms import ModelForm
from notes.models import Note

class NewNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

