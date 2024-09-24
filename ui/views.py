from django.shortcuts import render
from cust.forms import LoginForm, SignupForm
# Create your views here.
def login_page(request):
    if request.method == 'GET':
        return render(request=request,
                      template_name='login.html',
                      context={'login_form': LoginForm})

def signup_page(request):
    if request.method == 'GET':
        return render(request=request,
                      template_name='signup.html',
                      context={'signup_form': SignupForm})
    
def reset_password_page(request):
    if request.method == 'GET':
        return render(request=request,
                      template_name='reset_password.html')