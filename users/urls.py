from django.urls import path, include

from .views import (user_social_profile, user_list, send_friend_request, cancel_friend_request, accept_friend_request, delete_friend_request)

urlpatterns = [
    path('', user_list, name="user_list"),
    path('<int:pk>/', user_social_profile, name="user_social"),
    path('friend-request/send/<int:pk>/', send_friend_request, name="send_request"),
    path('friend-request/cancel/<int:pk>/', cancel_friend_request, name="cancel_request"),
    path('friend-request/accept/<int:pk>/', accept_friend_request, name="accept_request"),
    path('friend-request/delete/<int:pk>/', delete_friend_request, name="delete_request"),
] 