from django.shortcuts import render, redirect
from ..lognreg_app.models import LogNReg
from apps.optiong_app.models import *
from django.contrib import messages



def quotes(request):
    if request.method == "GET":

        context = {
            "user_info": LogNReg.objects.get(id = request.session["user_id"] ),
            "quotes": Quote.objects.order_by("-created_at"),
        }
        return render(request, "optiong_app/index.html", context)


def quotes_add(request):
    if request.method == "POST":
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/quotes")
        else:
            LogNReg_table_id = LogNReg.objects.get(id = request.session["user_id"])
            Quote.objects.create(
                users = LogNReg_table_id,
                authors = request.POST["author"],
                quotes = request.POST['text'],
            )
            return redirect("/quotes")

def quotes_likes(request,user_id, quotes_id):
    if request.method == "GET":
        quote_like = Quote.objects.get(id = quotes_id)
        user_likes = LogNReg.objects.get(id = user_id)
        quote_like.likes.add(user_likes)
        return redirect("/quotes")

def quotes_unlikes(request,user_id, quotes_id):
    if request.method == "GET":
        quote_like = Quote.objects.get(id = quotes_id)
        user_likes = LogNReg.objects.get(id = user_id)
        quote_like.likes.remove(user_likes)
        return redirect("/quotes")

