from django import forms 
from .models import PostModel, CommentModel




class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model =PostModel
        fields = ('title','content')



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':"Add your comment"}))
    class Meta:
        model = CommentModel
        fields = ('content',)
       
        