from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .forms import UserForm, ProfileForm
from .models import Profile, Follow, User
from django.contrib.auth import authenticate, login 
from django.urls import reverse
# Create your views here.

#User registration (add user)
def register(request): 
    context={}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user) 
            return HttpResponseRedirect( reverse('profile_view', args=[request.user.id]))
    
    context['form']=form 
    return render(request, "users/registration.html", context)

#User profile view 
def profile_view(request, user_id): 
    context = {}
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user = user)
    context['user'] = user
    context['profile'] = profile
    return render(request, "users/profile.html", context)

#Edit user profile 
def edit_profile(request, user_id):
    context = {}
    user = get_object_or_404(User, id = user_id)
    profile = get_object_or_404(Profile, user=user)
    
    profile_form = ProfileForm(request.POST or None, instance=profile)
    if profile_form.is_valid(): 
        profile_form.save()
        return redirect('profile_view', user_id = user.id)

    context['profile_form'] = profile_form
    return render(request, "users/edit.html", context)

#Follow a user 
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id = user_id) 
    if user_to_follow == request.user: 
        return render (request, "users/error.html", {'message': "You cannot follow yourself"})

    if not request.user.following.filter(id=user_id).exists(): 
        Follow.objects.create(follower = request.user, following = user_to_follow)
        return redirect('profile_view', user_id=user_id) 
    return render(request, "users/error.html", {"message": "You are already following that person"})

#Unfollow a user  
def unfollow_user(request, user_id): 
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if user_to_unfollow == request.user: 
        return render(request, "users/error.html", {"message": "You cannot unfollow yourself"})
    if request.user.following.filter(id=user_id).exists(): 
        request.user.following.filter(id=user_id).delete()
        return redirect('profile_view', user_id=user_id) 
    return render(request, "users/error.html", {"message": "You dont follow that person"})