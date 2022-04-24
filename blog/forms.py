from .models import Topic, Post, Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'title', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'name')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating', 'owner_name')
        labels = {'text': 'Comment', 'owner_name': 'Name'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'rows': 1})
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             max_length=64, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["username"].widget.attrs['placeholder'] = 'Username'
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs['placeholder'] = 'Password'
        self.fields["password2"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['placeholder'] = 'Password again'
