from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class LogNRegMessage(models.Manager):

    def login_validator(self, postData):
        
        login_errors = {}
    
        v_email = LogNReg.objects.filter(email=postData['login_email'])

        if len(v_email) == 0:
            login_errors["login_email"] = "Email Does not Exist"
        else:
            v_password = LogNReg.objects.get(email=postData['login_email']).password
            cur_password = postData['login_password']
            if not bcrypt.checkpw(cur_password.encode('utf8'), v_password.encode('utf8')):
                login_errors["login_password"] = "invalid password"
        return login_errors
        

    def edit_validator(self, postData):

        edit_errors = {}

        v_email = LogNReg.objects.filter(email = postData['email'])

        if len(postData['first']) < 1:
            edit_errors["first"] = "first name less than 2 characters"
        if len(postData['last']) < 1:
            edit_errors["last"] = "last name less than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            edit_errors["email"] = "Email format is not correct"
        if len(v_email) != 0:
            vr_email = LogNReg.objects.get(email = postData['email']).email
            if postData['email'] == vr_email:
                edit_errors["email"] = "Email have been used"
            

        
        return edit_errors



    def register_validator(self, postData):

        register_errors = {}

        v_email = LogNReg.objects.filter(email=postData['email'])
        
        if len(postData['first']) < 1:
            register_errors["first"] = "first name lass than 2 characters"
        if len(postData['last']) < 1:
            register_errors["last"] = "last name lass than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            register_errors["email"] = "Email format is not correct"
        if len(v_email) != 0:
            vr_email = LogNReg.objects.get(email = postData['email']).email
            if postData['email'] == vr_email:
                register_errors["email"] = "Email have been used"
        if 7 > len(postData['password']) >= 25:
            register_errors["password"] = "Password must have length 7-25"
        if postData['v_password'] != postData['password']:
            register_errors["v_password"] = "Password Doesn't match"
        
        
        return register_errors

# Create your models here.
class LogNReg(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LogNRegMessage()
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.password}"