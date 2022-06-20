from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('posteer')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users-login')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posteer')

    return auth_view.LoginView.as_view(template_name='users/login.html')(request)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
