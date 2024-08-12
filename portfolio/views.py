from django.shortcuts import render, redirect
from portfolio.forms import ContactForm, BlogStoryForm, CommentForm
from .models import BlogStory, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from portfolio.templatetags.functions import calculateReadTime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from portfolio.serializers import BlogSerializer
import json 


# Create your views here.
def index(response):
    return render(response, 'index.html')

def works(response):
    return render(response, 'works.html')

def contact(request):

    #send email form
    form = ContactForm()
	# if request.method == 'POST':
    #     message = request.POST['message']
	# 	send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['ivanovsin11@gmail.com'], fail_silently=False)


    context = {
        'form': form
    }
    return render(request, 'contact.html', context)



def blog(response):

    #print contents of database
    blog_stories = BlogStory.objects.all()
    blog_stories_json = BlogSerializer(blog_stories, many=True).data
    
    context = {
        'blog_stories': json.dumps(blog_stories_json)
    }

    return render(response, 'blog_crud/blog.html', context)


#Function to open Blog Story Template
def story(response, story_name):

    #get data from story based on story_name
    blog_story = BlogStory.objects.get(title = story_name)

    #Post request to send model form
    comment_form = CommentForm()

    #send to the view
    context = {
        'blog_story': blog_story,
        'comment_form': comment_form
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
            tags = form.cleaned_data['tags']

            new_story = BlogStory(title=title, caption=caption, story=story, imageUrl=imageUrl, tags=tags)    
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


#Like story button

def likeStory(request, story_name):

    if request.method == "POST":
        
        blog_story = BlogStory.objects.get(title = story_name)

        #increment blog stories
        blog_story.likes += 1
        #save is liked to cookies
        is_liked = True  

        blog_story.save()

        # Render a partial HTML snippet with updated content
        return render(request, 'components/like_button.html', {'blog_story': blog_story, 'is_liked': is_liked})


#function to post comment in story()
def create_comment(request, story_name):
    if request.method == 'POST':
        blog_story = BlogStory.objects.get(title = story_name)
        form = CommentForm(request.POST)

        if form.is_valid():
            # Save the comment to the database
            comment = form.save(commit=False)
            comment.blog_story = blog_story
            comment.save()

            # Render the updated comments section
            return render(request, 'components/comment_section.html', {'blog_story': blog_story})




#function to delete comment
def delete_comment(request, story_name, comment_id):

    #get blog story
    blog_story = BlogStory.objects.get(title = story_name)
    #get certain comment
    comment = Comment.objects.get(id = comment_id, blog_story=blog_story)

    # Delete the comment
    comment.delete()

    #return successful json response
    return render(request, 'components/comment_section.html', {'blog_story': blog_story})


