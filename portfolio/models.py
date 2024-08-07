from django.db import models
from django.utils.timezone import now

# Create your models here.

class BlogStory(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    story = models.TextField()
    imageUrl = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(default=now, editable=False)
    likes = models.IntegerField(default=0)  

    def __str__(self):
        return self.title 

# Tags in future
# Comments in future


