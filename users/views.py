from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    """
        View for user registration.

        Checks if a user request is a POST or GET.
        If it is a POST request, it creates an instance
        of the user register form and pass in the user's
        POST request. If it is a GET request, it just 
        displays the user register form for the user.

        It then checks if the form is valid. If it is valid,
        it saves the data in the database and sends the user 
        to the login page and diplays a success message. 
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!\
                            You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    template_name = 'users/register.html'
    
    return render(request, template_name, context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    template_name = 'users/profile.html'

    return render(request, template_name, context)
