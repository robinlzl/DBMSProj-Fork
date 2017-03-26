from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.


def default(request):
    return render_to_response("main.html")

def navigator(request, direction):
    try:
        to = direction
    except ValueError:
        raise Http404
    if to == 'home':
        return render(request, "main.html")
    elif to == 'account':
        return render(request, "account_info.html")
    elif to == 'travel':
        return render(request)
    elif to == 'about':
        return render(request)
    elif to == 'signin':
        return render(request, "signin.html")
    elif to == 'register':
        return render(request, "register.html")
    elif to == 'signout':
        logout(request)
        return render(request, "main.html")


@csrf_exempt
def register(request):

    try:
        User.objects.create_user(first_name=request.POST['firstname'],
                                     last_name=request.POST['lastname'],
                                     email=request.POST['email'],
                                     password=request.POST['pwd'],
                                     username=request.POST['email'],)
        u = User.objects.get(username=request.POST['email'])
        ud = User_Detail(user=u,
                         state=request.POST['state'],
                         address=request.POST['address'],
                         city=request.POST['city'],
                         zipcode=request.POST['zipcode'], )
        ud.save()

        if u.is_active:
            login(request=request, user=u)

    except Exception:
        return render(request, "info.html",
                      {"isError": 1, "info_msg": "Account is NOT exist or Password is NOT correct."})
    return render(request, "info.html", {"isSuccess": 1, "info_msg": "Success!"})


@csrf_exempt
def signin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, "info.html", {"isSuccess": 1, "info_msg": "Sign in Successfully"})
    else:
        return render(request, "signin.html", {"isError": 1, "info_msg": "Account is NOT exist or Password is NOT correct."})


def account_navigator(request, direction):
    try:
        to = direction
        u = request.user
        ud = User_Detail.objects.get(user_id=u.id)
    except ValueError:
        raise render(request, "info.html", {"isError": 1, "info_msg": "Error"})
    if to == 'info':
        return render(request, "account_info.html", {"show_id": 1, "state": ud.state, "zipcode": ud.zipcode, "city": ud.city, "address": ud.address})
    elif to == 'infomodify':
        return render(request, "account_info.html", {"show_id": 2, "ud": ud})
    elif to == 'pwdmodify':
        return render(request, "account_info.html", {"show_id": 3})
    elif to == 'travel':
        return render(request)


@login_required(login_url='/navigator/signin/')
def user_modify(request):
    u = request.user


@csrf_exempt
def pwd_modify(request):
    try:
        old_password = request.POST['cpwd']
        new_password = request.POST['npwd']

        user = authenticate(username=request.user.email, password=old_password)
        u = User.objects.get(username=request.user.email)
    except ValueError:
        raise render(request, "info.html", {"isError": 1, "info_msg": "Error"})
    if user is not None:
        u.set_password(new_password)
        u.save()
        logout(request)
        return render(request, "info.html", {"isSuccess": 1, "info_msg": "Password modify Successfully. Please signin again."})
    else:
        return render(request, "account_info.html", {"show_id": 3, "error_info": "Your password is NOT correct."})


