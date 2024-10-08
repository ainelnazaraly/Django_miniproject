from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

#List all posts 
def post_list(request): 
    context = {}
    context["dataset"] = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", context)

#View a single post 
def post_detail(request, id): 
    context = {}
    context["data"] = Post.objects.get(id = id)
    return render(request, "blog/post_detail.html", context)

#Create a new post 
def create_post(request):
    context = {}
    
    form=PostForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return redirect('post_list')
    
    context["form"] = form 
    return render(request, "blog/post_form.html", context)

#Edit post 
def update_post(request, id): 
    context={}

    obj = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance= obj)

    if form.is_valid(): 
        form.save()
        return redirect("post_detail", id=id)

    context["form"] = form

    return render(request, "blog/update_post.html", context)

#Delete a post 
def delete_post(request, id):
    obj = get_object_or_404(Post, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("post_list") 

    return render(request, "blog/post_list.html", {}) 

#List comments for a post 
def comment_list(request, post_id): 
    context = {}
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    
    context["comments"] = comments

    return render(request, "blog/post_detail.html", context)

#Add comment to a post 
def add_comment(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST": 
        form = CommentForm(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False)
            comment.post = post 
            comment.author = request.user
            comment.save()
            return redirect('post_detail', id=post.id) 
        
    else:
        form = CommentForm()  
    
    context = {
        "post": post,
        "form": form,
    }
    
    return render(request, "blog/comment_form.html", context)