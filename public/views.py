from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

def index_view(request):
    return redirect('public:home')

def public_home(request):
    return render(request, 'index.html')

def public_login(request):
    if request.method != 'POST':
        return render(request, 'public/login.html')
    else:
        phone  = request.POST['phone_number']                                            #get PHno
        passwd = request.POST['password']                                                #get passwd
        if phone.isnumeric() and len(phone)==10:
            user   = authenticate(username=phone, password=passwd)                       #validating function 
            if user is not None:
                login(request, user)
                if user.is_authenticated and user.is_superuser == True:
                    return redirect('admin_app:dashboard')
                else:
                    messages.error(request, 'This User is not Admin')
                    return redirect('public:login')
            else:
                messages.error(request,'Invalid Credantials!')
                return redirect('public:login')
        else:
            messages.error(request, 'Invalid Phone Number (Must be 10 digit)!')
            return redirect('public:login')

def logout_view(request):
    request.session.flush()
    logout(request)
    return HttpResponseRedirect('/')