# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Friend
from ..loginreg.models import User
from django.shortcuts import render, redirect, HttpResponse
import timeago, datetime
def index(request):
    #User.userManager.all().delete()
    #Friend.friendManager.all().delete()
    if request.session['loggedin'] == "false":
        print "equals false"
        return redirect ("/login")
    else:
        start = User.userManager.all()
        print "equals true"
        context = {
        'name': request.session["first_name"],
        'user': start.order_by("-created_at")[:3]
        }
    return render(request, 'friends/index.html', context)

def addfriend(request):
    if request.session['loggedin'] == "false":
        return redirect ("/login")
    else:
        get_user = User.userManager.exclude(id = request.session["user_id"]).all()
        get_friend = Friend.friendManager.filter(user_id = request.session["user_id"])
        context = {
        'name': request.session["first_name"],
        'friends': get_user,
        'friends2': get_friend
        }
    return render(request, 'friends/addfriends.html', context)

def currentfriend(request):
    if request.session['loggedin'] == "false":
        return redirect ("/login")
    else:
        get_user = Friend.friendManager.filter(user_id = request.session["user_id"])
        context = {
        'name': request.session["first_name"],
        'curfriends': get_user
        }
    return render(request, 'friends/currentfriends.html', context)

def addfriendlogic(request, id):
    if request.session['loggedin'] == "false":
        return redirect ("/login")
    else:
        Friend.friendManager.addfriend(User.userManager.filter(id = id).first(), User.userManager.get(id = request.session["user_id"]))
    return redirect('/home')

def deletefriend(request, id):
    if request.session['loggedin'] == "false":
        return redirect ("/login")
    else:
        Friend.friendManager.addfriend(User.userManager.filter(id = id).first(), User.userManager.get(id = request.session["user_id"]))
    return redirect('/home')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    request.session['loggedin'] = 'false'
    return redirect('/login')
