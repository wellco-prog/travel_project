from django import forms
from .models import Comment


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Your comment',
                                                  'class': 'form-control'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Keyword','class':'form-control'}))
