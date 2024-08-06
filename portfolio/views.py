from django.shortcuts import render
from users.forms import ContactForm

# Create your views here.
def index(response):
    return render(response, 'index.html')

def works(response):
    return render(response, 'works.html')

def contact(response):
    form = ContactForm()

    context = {
        'form': form
    }
    return render(response, 'contact.html', context)

def blog(response):
    return render(response, 'blog.html')

def story(response):
    return render(response, 'blog_template.html')

def create(response):
    return render(response, 'create_blog.html')
