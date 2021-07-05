from django import forms
from django.forms import fields
from .models import Post  # dot means current directory

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


