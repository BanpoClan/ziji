from django.shortcuts import render


def index(req):
    return render(req, "index.html")


def main_page(req):
    return render(req, "dashboard.html")
