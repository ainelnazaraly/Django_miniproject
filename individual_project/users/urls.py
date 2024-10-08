from django.urls import path
from .views import register, profile_view,  edit_profile, follow_user, unfollow_user

urlpatterns=[
    path('register/', register, name='register'), 
    path('profile/<int:user_id>', profile_view, name = 'profile_view'),
    path('profile/edit/<int:user_id>', edit_profile, name='edit_profile'), 
    path('follow/<int:user_id>', follow_user, name='follow_user'), 
    path('unfollow/<int:user_id>', unfollow_user, name='unfollow_user'), 
    


]
