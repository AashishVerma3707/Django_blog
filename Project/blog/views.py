from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from .import Model_forms

def func1(request):
    article= Article.objects.all()

    return render(request, "index.html",{"article":article})


@login_required(login_url="/accounts/log_in")
def func2(request):
    if request.method=='POST':
        forms=Model_forms.Create_article(request.POST, request.FILES)
        if forms.is_valid():
            instance=forms.save(commit=False)
            instance.input_by= request.user
            instance.save()

            return redirect('/blog/list')
    else:
        forms=Model_forms.Create_article()
    return render(request,'index3.html',{"forms":forms})


def details(request,slug):
    Got_article=Article.objects.get(slug=slug)
    return render(request,"index2.html",{"Got_article":Got_article})

def Update_blog(request,pk):
    b_log=Article.objects.get(id=pk)
    form=Model_forms.Create_article(instance=b_log)
    if request.method=="POST":
        form=Model_forms.Create_article(request.POST, instance=b_log)
        if form.is_valid():
            form.save()
            return redirect('/blog/list')
    return render(request , "Update_blog.html" , {"form":form,"pk":pk})
def Delete_blog(request , pk):
    b_log=Article.objects.get(id=pk)
    if request.method=="POST":
        b_log.delete()
        return redirect('/blog/list')
    return render(request, "Delete_blog.html" , {"b_log":b_log,"pk":pk})

