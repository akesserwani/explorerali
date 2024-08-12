from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.

class BlogStory(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    story = RichTextField(blank=True, null=True)
    imageUrl = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(default=now, editable=False)
    likes = models.IntegerField(default=0)  

    tags = models.CharField(max_length=200, blank=True) 

    def __str__(self):
        return self.title 

class Comment(models.Model):
    blog_story = models.ForeignKey(BlogStory, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50) 
    email = models.CharField(max_length=50, blank=True) 
    comment = models.TextField()
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.author_name

