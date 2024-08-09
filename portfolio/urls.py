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

    #crud functionalities for deleting and updating comments
    path('comment/<str:story_name>', views.create_comment, name = "post_comment"),
    path('comment/<str:story_name>/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]