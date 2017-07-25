# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class UserManager(models.Manager):
    def login(self, postData):
        if postData['email'] != "" and postData['password'] != "":
            self.email = postData['email']
            self.password = postData['password']
        else:
            return "error"
        if User.userManager.filter(email = postData['email'], password = postData['password']):
            get_user = User.userManager.filter(email = postData['email'], password=postData['password']).first()
            name = get_user.id
            return name
        else:
            return "error"

    #def register(self, first_name, last_name, email, password, confirm_password):
    def register(self, postData):
        print postData['first_name']
        if postData['first_name'] != "" and postData['last_name'] != "" and postData['email'] != "" and postData['password'] != "" and postData['confirm_password'] != "":
            pass
        else:
            return "error"
        if User.userManager.filter(email = postData['email']):
            return "existserror"
        if postData['password'] == postData['confirm_password']:
            self.first_name = postData['first_name']
            self.last_name = postData['last_name']
            self.email = postData['email']
            self.password = postData['password']
            User.userManager.create(first_name = self.first_name, last_name = self.last_name, email = self.email, password = self.password)
            return self
        else:
            return "passerror"

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    userManager = UserManager()
    # *************************

# Create your models here.
