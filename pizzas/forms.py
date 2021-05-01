from django import forms
from .models import Pizza, Topping, Comment


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["text"]
        labels = {"Text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ["text"]
        label = {"Text:": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        label = {"Text:": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
