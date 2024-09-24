from django.shortcuts import render, HttpResponse
from django.contrib import auth

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        usr = request.POST.get('user_name')
        pwd = request.POST.get('password')
        user = auth.authenticate(username=usr, password=pwd)
        if user:
            auth.login(request, user)
            return render(request=request,
                          template_name='profile.html')
        return HttpResponse("Login Failed, <a href='/'>Login again</a>")