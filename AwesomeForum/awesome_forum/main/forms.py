from .models import Post, Comments
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Start typing'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Start typing...'
            })
        }
