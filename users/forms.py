from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, ModelForm


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your Email"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Message"}))

class CreateBlog(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Story Title"}))
    caption = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Story Caption"}))
    story = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Write Story Here"}))
