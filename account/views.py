from django.contrib.auth import authenticate, login
from django.shortcuts import render

from django.http import HttpResponse

from account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user:
                if user.is_acitve:
                    login(request,user)
                    return HttpResponse('Authenticate successfully')
                else:
                    return HttpResponse('Disable acc')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

