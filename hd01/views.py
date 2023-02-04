from django.shortcuts import render, HttpResponse
import json


# Create your views here.
def login(request):
    return HttpResponse('登陆成功')


def user_list(request):
    user_name = 'hudi'
    return render(request, "user.html", {'user': user_name})


def pic(request):
    return render(request, "pic.html")


def duiduidui(request):
    if request.method == 'get':
        return None
