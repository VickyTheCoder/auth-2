from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.forms.models import model_to_dict

import traceback
from cust.forms import LoginForm


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
    
def logout_user(request):
    auth.logout(request)
    return render(request=request,
                  template_name='profile.html')

def add_user(request):
    error = None # Assumes the user creation is positive
    if request.method == 'POST':
        usr = request.POST.get('user_name')
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        if pwd != pwd2:
            error = "Passwords dont match.." # could be moved to JS
        else:
            # to catch an DB/auth issues
            try:
                user = auth.models.User.objects.create_user(username=usr,
                                    password=pwd)
                if user:# if signup successful?
                    auth.login(request, user) # logins
                    # to check if username is shown in profile page
                    return render(request=request,
                              template_name='profile.html')
                else:
                    error = 'Fill the form carefully'
            except Exception as e:
                print(traceback.format_exc())# to debug
                error = str(e)
        return HttpResponse(f"Signup Failed due to <b>{error}</b><br><a href='/signup'>Signup again</a>")

def reset_password(request):
    error = None # Assumes the user's password change is positive
    if request.method == 'POST':
        usr = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        pwd2 = request.POST.get('pwd2')
        user = auth.authenticate(username=usr, password=pwd)
        if user:# user is eligible to change password
            u = auth.models.User.objects.get(username=usr)
            u.set_password(pwd2)
            u.save()
        else:
            error = "Invalid User"
        if error is None:
            # to check if the changed password works
            return render(request=request,
                          template_name='login.html',
                          context={'login_form': LoginForm})
        return HttpResponse(f"Reset Password Failed due to <b>{error}</b><br><a href='/reset/password'>Try again</a>")

@auth.decorators.login_required(login_url='/')
def cust_details(request):
    user = request.user
    u = auth.models.User.objects.get(pk=user.id)
    ud = model_to_dict(u)
    ud.pop('id')
    ud.pop('password')
    return render(request=request,
                  template_name='user_details.html',
                  context={'ud': ud})