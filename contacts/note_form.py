from django.forms import ModelForm, Textarea
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        widgets = {"note": Textarea (attrs = {"cols":80, "rows":20})}
        model = Note
        fields = [
            'note_name'
        ]