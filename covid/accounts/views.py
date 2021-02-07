from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterform
def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, "Hello, {}. You are.".format({username}))
            return redirect('login')
    else:
        form=UserRegisterform()
    return render(request,'accounts/register.html',{'form':form})
