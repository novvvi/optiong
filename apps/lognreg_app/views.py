from django.shortcuts import render, redirect
from apps.lognreg_app.models import *
from django.contrib import messages
from ..optiong_app.models import *
import bcrypt



def lognreg(request):
    if request.method == "GET":

        if "user_id" in request.session:
            loginout = "logout"
        else: 
            loginout = "login"



        context = {
            "loginout" : loginout
        }
        return render(request, "lognreg_app/login.html", context)



def user(request, id):
    if request.method == "GET":
        context = {
            "user_info" : LogNReg.objects.get(id = id),
            "quotes" : Quote.objects.all()
        }
        return render(request, "lognreg_app/index.html", context)



def myaccount(request, id):
    if request.method == "GET":
        context = {
            "user_info" : LogNReg.objects.get(id = id)
        }
        return render(request, "lognreg_app/edit.html", context)


def myaccount_update(request):
    if request.method == "POST":
        errors = LogNReg.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/myaccount/{request.session['user_id']}")
        else:
            print ("updated")
            user_get = LogNReg.objects.get(id = request.session['user_id'])
            user_get.first_name = str(request.POST['first'])
            user_get.last_name = str(request.POST['last'])
            user_get.email = str(request.POST['email'])
            user_get.save()
            return redirect(f"/myaccount/{request.session['user_id']}")





def logout(request):
    if request.method == "GET":
        request.session.clear()
        return redirect("/")


def lognreg_login(request):
    if request.method == "POST":
        errors = LogNReg.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            user_get = LogNReg.objects.get(email = request.POST["login_email"])
            request.session["user_id"] = user_get.id
            return redirect("/quotes")




def lognreg_register(request):
    if request.method == "POST":
        errors = LogNReg.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            post_password_bcrypt = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt())
            print (post_password_bcrypt)
            LogNReg.objects.create(
                first_name = request.POST["first"],
                last_name = request.POST["last"],
                email = request.POST["email"],
                password = post_password_bcrypt
            )
            user_get = LogNReg.objects.get(email = request.POST["email"])
            request.session["user_id"] = user_get.id
            return redirect("/quotes")

