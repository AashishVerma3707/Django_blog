
from django.urls import path
from . import views



app_name = "blog"

urlpatterns = [
    path(r'list', views.func1 , name="bloghome"),
    path(r"create/", views.func2, name="blogcreate"),

    path(r'^(?P<slug>[\w-]+)$', views.details, name="blogdetails"),
    path('Update_blog/<str:pk>/',views.Update_blog, name="Update_blog"),
path('Delete_blog/<str:pk>/',views.Delete_blog, name="Delete_blog")

         ]