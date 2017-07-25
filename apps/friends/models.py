# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from friends.apps.loginreg.models import User
class FriendManager(models.Manager):
    def deletefriend(self, postData):
        pass

    #def register(self, first_name, last_name, email, password, confirm_password):
    def addfriend(self, postData, user):
        print user.id
        Friend.friendManager.create(first_name = postData.first_name, last_name = postData.last_name, user_id = user)

class Friend(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user_id = models.ForeignKey('loginreg.User')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.first_name + " " + self.last_name

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    friendManager = FriendManager()
    # *************************

# Create your models here.
