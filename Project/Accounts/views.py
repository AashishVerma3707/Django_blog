from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def func1(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('blog:bloghome')
    else:
        form=UserCreationForm()

    return render(request, "Accounts/signup.html",{"form":form})
def func2(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('blog:bloghome')
    else:
        form=AuthenticationForm()
    return render(request, "Accounts/log_in.html",{"form":form})

def func3(request):
    if request.method=='POST':
        logout(request)
        return redirect('blog:bloghome')