
from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path(r'list', views.func1 , name="bloghome"),
    path(r"create/", views.func2, name="blogcreate"),

    path(r'^(?P<slug>[\w-]+)$', views.details, name="blogdetails")

         ]