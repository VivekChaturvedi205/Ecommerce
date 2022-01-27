from django.shortcuts import render
from main.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from . inherit import cartData
import json


def Index(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    data = Product.objects.all()
    return render(request, 'main/Base.html', {'data': data, 'cartItems': cartItems})


def login(request):
    return render(request, 'main/Login.html')


def Reg(request):
    return render(request, 'main/Registration.html')


def Reg_Process(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            username = request.POST['UserName']
            name = request.POST['Name']
            Password = request.POST['Password']
            Password1 = request.POST['AgainPassword']
            email = request.POST['Email']
            phone = request.POST['Phone']

            if Password == Password1:
                try:
                    user = User.objects.get(username=request.POST['UserName'])
                    return render(request, 'main/Registration.html', {'error': "Username Already Exist"})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=username, password=Password)
                    customers = Customer.objects.create(
                        user=user, name=name, email=email, phone_number=phone)
                    user.save()
                    customers.save()
                    return redirect("/main/login")
            else:
                return render(request, 'main/Registration.html', {'error': "Password Don't Match"})
        else:
            return render(request, 'main/Registration.html')


def login_Process(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        user = auth.authenticate(username=UserName, password=Password)
        if user is not None:
            auth.login(request, user)
            request.session['UserName'] = UserName
            return redirect("/")
        else:
            return render(request, 'main/Login.html', {'error': "Invalid Login Credentails!!"})
    else:
        render(request, 'main/Login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def change(request):
    return render(request, 'main/Changepassword.html')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("main/login")
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                return redirect("/")
            else:
                return redirect("main/change_password")
        except:
            pass
    return render(request, 'main/change.html')


def search(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    if request.method == "POST":
        search = request.POST['search']
        data = Product.objects.filter(Name__contains=search)
        return render(request, 'main/Base.html', {'data': data, 'search': search, 'cartItems': cartItems})
    else:
        return render(request, 'main/Base.html')
