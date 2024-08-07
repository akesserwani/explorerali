from django.shortcuts import render, redirect
from users.forms import ContactForm, BlogStoryForm
from .models import BlogStory
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    #print contents of database
    blog_stories = BlogStory.objects.all()

    context = {
        'blog_stories': blog_stories
    }

    return render(response, 'blog_crud/blog.html', context)


#Function to open Certain Blog Story
def story(response, story_name):

    #get data from story based on story_name
    blog_story = BlogStory.objects.get(title = story_name)
    #send to the view
    context = {
        'blog_story': blog_story
    }

    return render(response, 'blog_crud/story_blog.html', context)



#Function to Create Blog Story
@login_required
def create(response):
    form = BlogStoryForm()
    #create new map
    if response.method == "POST":
        form = BlogStoryForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            caption = form.cleaned_data['caption']
            story = form.cleaned_data['story']
            imageUrl = form.cleaned_data['imageUrl']

            new_story = BlogStory(title=title, caption=caption, story=story, imageUrl=imageUrl)    
            new_story.save()        

            messages.success(response, 'Story has been created!')
            return redirect('blog')

        else: 
            #throw error if map already exists
            # messages.error(response, f'Map name already exists.')
            print("Unsuccessful")
            return redirect('blog')
    else:
        form = BlogStoryForm()

    context = {
        'form': form
    }

    return render(response, 'blog_crud/create_blog.html', context)

@login_required
def edit(request, story_name):
    current_story = BlogStory.objects.get(title = story_name)

    updateStoryForm = BlogStoryForm(instance=current_story)

    #if the button clicked is update_story then update the story
    if request.method == 'POST' and 'update_story' in request.POST:
        updateStoryForm = BlogStoryForm(request.POST, instance=current_story)
        if updateStoryForm.is_valid():
            # This automatically saves the updated instance
            updateStoryForm.save()
            #give message
            messages.success(request, 'Story has been updated!')
            # Redirect to a success page or the updated story's detail view
            return redirect('blog_story', story_name=current_story.title)
        
    #if the button clicked is delete_story then delete the story
    elif request.method == 'POST' and 'delete_story' in request.POST:
        #logic to delete the story 
        current_story.delete()
        #give message
        messages.error(request, 'Story has been deleted')
        #redirect to blog home page
        return redirect('blog')

    else:
        updateStoryForm = BlogStoryForm(instance=current_story)



    context = {
        'form': updateStoryForm,
        'current_story': current_story
    }

    return render(request, 'blog_crud/edit_blog.html', context)
