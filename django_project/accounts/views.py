from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import \
    AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm,UserProfileForm, ChangePasswordForm
from django.contrib.auth.hashers import check_password


from django.contrib.auth.models import User


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return redirect(
                        'accounts:profile')  # TODO: go to profile

                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return redirect('accounts:profile')
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST,
                             instance=request.user)
        profile_form = UserProfileForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been edited.")
            return redirect('accounts:profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form,
                                                     'profile_form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been changed.")
            return redirect('accounts:profile')

    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
