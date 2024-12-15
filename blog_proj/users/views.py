from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def sign_up (request):
    if request.method == 'POST':  
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users-login')

    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'users/sign_up.html', context)



def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')


@login_required
def ProfileView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None,instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid()  and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context ={
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request,'users/profile.html',context)