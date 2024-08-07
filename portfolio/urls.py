from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('works/', views.works, name = "works"),
    path('contact/', views.contact, name = "contact"),
    path('blog/', views.blog, name = "blog"),

    path('blog/story/<str:story_name>', views.story, name = "blog_story"),

    path('blog/create', views.create, name = "blog_create"),

    path('blog/edit/<str:story_name>', views.edit, name = "blog_edit"),

    path('like/<str:story_name>', views.likeStory, name = "like_story"),

]