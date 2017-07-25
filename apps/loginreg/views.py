# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import User, UserManager

def index(request):
    try:
        if request.session["loggedin"] == "true":
            return redirect ("/home")
    except KeyError:
        request.session["loggedin"] = "false"
    return render(request, "loginreg/index.html")

def verify(request):
    if request.method == "POST":
        try:
            request.POST['register_button']
            rtrn = User.userManager.register(request.POST)
            if rtrn == "passerror":
                messages.add_message(request, messages.INFO, "(Passwords Do Not Match)")
                return HttpResponseRedirect ("/login")
            elif rtrn == "existserror":
                messages.add_message(request, messages.INFO, "(User Already Exists)")
                return HttpResponseRedirect ("/login")
            elif rtrn == "error":
                messages.add_message(request, messages.INFO, "(Fields Incomplete)")
                return HttpResponseRedirect ("/login")
            else:
                messages.add_message(request, messages.INFO, "Thanks for Registering, Please Login")
                #request.session["loggedin"] = "true"
                request.session["first_name"] = request.POST['first_name']
                return redirect ("/login")
        except KeyError:
            pass
        try:
            request.POST['login_button']
            rtrn = User.userManager.login(request.POST)
            if rtrn == "error":
                messages.add_message(request, messages.INFO, "(Email and Password Does Not Match)")
                return HttpResponseRedirect ("/login")
            else:
                request.session["loggedin"] = "true"
                get_user = User.userManager.filter(id = rtrn).first()
                name = get_user.first_name
                user_id = get_user.id
                request.session["user_id"] = user_id
                request.session["first_name"] = name
                return redirect ("/home")
        except KeyError:
            pass
