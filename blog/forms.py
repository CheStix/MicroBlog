from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Форма добавления сообщения"""

    class Meta:
        model = Post
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'})}
