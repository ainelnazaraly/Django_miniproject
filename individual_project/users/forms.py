from django import forms
from .models import Profile, Follow, User

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile 
        fields ="__all__"

class FollowForm(forms.ModelForm): 
    class Meta: 
        model = Follow 
        fields = "__all__"

class UserForm(forms.ModelForm): 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password']
