from django.contrib import admin

# Register your models here.

from notes.models import Note, Comment

class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
    )

admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)
