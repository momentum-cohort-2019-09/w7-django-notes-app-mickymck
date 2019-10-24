from django.forms import ModelForm
from notes.models import Note
# from notes.models import Comment

class NewNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']


# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comment']
