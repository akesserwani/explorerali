

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [

    path("__reload__/", include("django_browser_reload.urls")),

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "logout.html"), name = "logout"),

    path ('', include('portfolio.urls'))


]
