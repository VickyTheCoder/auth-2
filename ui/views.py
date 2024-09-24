from django.shortcuts import render
from cust.forms import LoginForm 
# Create your views here.
def login_page(request):
    if request.method == 'GET':
        return render(request=request,
                      template_name='login.html',
                      context={'login_form': LoginForm})