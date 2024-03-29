from django import forms
from .models import Pizza, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        label = {"Text:": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
