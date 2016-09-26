from django.shortcuts import render


def login(req):
    return render(req, "login.html")

def login_action(req):
    return render(req, "login.html")

