from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm
from portfolio.models import BlogStory


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your Email"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Message"}))

class BlogStoryForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Story Title"}))
    caption = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter Story Caption"}))
    story = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Write Story Here", 'rows':15, 'cols':20}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Image Url"}))


    class Meta:
        model = BlogStory
        fields = ['title', 'caption', 'story', 'imageUrl']
