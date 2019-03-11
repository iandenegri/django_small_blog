from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, FriendRequest

User = get_user_model()

# Create your views here.

def register(request):
    if request.method=="GET":
        form = UserRegisterForm()
    elif request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You may now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form':form})

@login_required
def profile(request):
    prof = Profile.objects.filter(user=request.user).first()
    profile_user = prof.user

    sent_fre_requests = FriendRequest.objects.filter(from_user=profile_user)
    rec_fre_requests = FriendRequest.objects.filter(to_user=profile_user)

    friends = prof.friends.all()

    if request.method=="POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Account details have been updated.")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form":user_form,
        "profile_form":profile_form,
        "profile_user":profile_user,
        "sent_requests":sent_fre_requests,
        "rec_requests":rec_fre_requests,
        "friends_list":friends,
        "profile":prof,
    }
    
    return render(request, "users/profile.html", context=context)

@login_required
def user_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        "profiles": profiles
    }
    return render(request, "users/user_list.html", context=context)

@login_required
def send_friend_request(request, id):
    if request.user.is_authenticated():
        user_recipient = get_object_or_404(User, id=id) # Passing the id of the user we're trying to find and add.
        fri_request, created = FriendRequest.objects.get_or_create(
            from_user = request.user,
            to_user = user_recipient
        )
        messages.success(request, "Your friend request to {} has been sent!.".format(user_recipient))
        return redirect('/')

@login_required
def cancel_friend_request(request, id):
    if request.user.is_authenticated():
        user_recipient = get_object_or_404(User, id=id) # Passing the id of the user we're trying to find and add.

        fri_request = FriendRequest.objects.filter(
            from_user = request.user,
            to_user = user_recipient
        ).first() # Find a queryset of objects that match the to and from users (there should only be one..) and then pick the first object so it's a model object and not a queryset.

        fri_request.delete()
        messages.success(request, "Your friend request to {} has been canceled!.".format(user_recipient))
        return redirect('/')

@login_required
def accept_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)

    fri_request = FriendRequest.objects.filter(
        from_user = from_user,
        to_user = request.user
    ).first() # Find QS that matches to from, pick first obj of QS so it's an obj and not a QS.

    user1 = fri_request.to_user
    user2 = fri_request.from_user
    user1.profile.friends.add(user2.Profile)
    user2.profile.friends.add(user1.Profile)
    fri_request.delete()
    messages.success(request, "Your friend request from {} has been accepted!.".format(from_user))
    return redirect('/profile/')

@login_required
def delete_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)

    fri_request = FriendRequest.objects.filter(
        from_user = from_user,
        to_user = request.user
    ).first() # Find QS that matches to from, pick first obj of QS so it's an obj and not a QS.

    fri_request.delete()
    messages.success(request, "Your friend request from {} has been deleted!.".format(from_user))
    return redirect('/profile/')

def user_social_profile(request, pk):
    prof = Profile.objects.filter(pk=pk).first()
    profile_user = prof.user

    sent_fre_requests = FriendRequest.objects.filter(from_user=profile_user)
    rec_fre_requests = FriendRequest.objects.filter(to_user=profile_user)

    friends = prof.friends.all()

    button_status = 'none'
    # Check to see if this user is your friend
    if prof not in request.user.profile.friends.all():
        button_status = 'not_friend'

        if FriendRequest.objects.filter(from_user=request.user).filter(to_user=profile_user):
            button_status = 'request_sent'
    context = {
        'user':profile_user,
        'button_status':button_status,
        'friends_list':friends,
        'sent_requests':sent_fre_requests,
        'rec_requests':rec_fre_requests
    }
    return render(request, 'users/user_social_profile.html', context=context)
