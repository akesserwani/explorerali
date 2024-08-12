from rest_framework.serializers import ModelSerializer
from portfolio.models import BlogStory

class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogStory
        fields = ('title', 'caption', 'story', 'imageUrl', 'created_date', 'likes', 'tags')