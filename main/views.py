from django.shortcuts import render
from main.models import Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def Index(request):
    data=Product.objects.all()
    context={'data':data}
    return render(request, 'main/Base.html',context)
    
def login(request):
    return render(request, 'main/Login.html')

def Reg(request):
    return render(request, 'main/Registration.html')

def Reg_Process(request):
    if request.method=='POST':
        if request.POST['Password'] == request.POST['AgainPassword']:
            try:
                user=User.objects.get(username=request.POST['UserName'])
                return render(request,'main/Registration.html',{'error':"Username Already Exist"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['UserName'],password=request.POST['Password'])
                return redirect("/main/login")
        else:
            return render(request,'main/Registration.html',{'error':"Password Don't Match"})
    else:
        return render(request, 'main/Registration.html')

def login_Process(request):
    if request.method=='POST':
        UserName=request.POST['UserName']
        Password=request.POST['Password']
        user=auth.authenticate(username=UserName,password=Password)
        if user is not None:
            auth.login(request,user)
            request.session['UserName']=UserName
            return redirect("/")
        else:
            return render(request,'main/Login.html',{'error':"Invalid Login Credentails!!"})
    else:
        render(request,'main/Login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
