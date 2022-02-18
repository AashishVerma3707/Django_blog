
from django.urls import path
from . import views
app_name = "Accounts"

urlpatterns = [
    path(r'sign_up', views.func1 , name="Signup_page"),
path(r'log_in', views.func2 , name="Login_page"),
path(r'log_out', views.func3 , name="Logout_page")

]