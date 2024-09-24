from django.shortcuts import render, HttpResponse
from django.contrib import auth
import traceback

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
        