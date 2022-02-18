"""History URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import Views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from blog import views as blog_views
# from django.conf.urls import url
from blog.api import ArticleBody, ArticleBodyDetail, UserAuthentication
from django.views.static import serve


app_name = "Histor"
urlpatterns = [
    path('admin/', admin.site.urls),
path("", blog_views.func1,name="home"),
    path("blog/",include("blog.urls")),
    path("accounts/",include("Accounts.urls")),
    re_path(r'^api/article_body/$', ArticleBody.as_view() ,name="article_body"),
re_path(r'^api/article_body/(?P<employee_id>\d+)/$', ArticleBodyDetail.as_view() , name="article_body_detail"),
re_path(r'^api/auth/$', UserAuthentication.as_view() ,name="User_Authentication"),
re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

