from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts,
        
    }
    return render(request,'blog/list.html',context)
def post_detail(request,pk):
    #print(pk)
    post = Post.objects.get(id=pk)
    #print(post)
    context = {
        'post':post
    }
    return render(request,'blog/detail.html',context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog/")
    context = {
        "form":form
    }
    return render(request,"blog/post_create.html",context)

def post_update(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog")
    context = {
        "form":form,
        "post":post
    }
    return render(request,"blog/update.html",context)

def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect ("/blog")

