from django.shortcuts import render, HttpResponse
import json
import time


# Create your views here.
def login(request):
    return HttpResponse('登陆成功')


def user_list(request):
    user_name = 'hudi'
    return render(request, "user.html", {'user': user_name})


def pic(request):
    return render(request, "pic.html")


def git(request):
    if request.method == 'get':
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')


def you_money(request):
    if request.method == 'POST':
        begin_time = request.POST.get('begin_time')
        over_time = request.POST.get('over_time')
        money = request.POST.get('money')
        hour = request.POST.get('hour')
        data = request.POST.get('data')
        while True:
            t = time.localtime()
            now_sec = int(t.tm_hour) * 3600 + int(t.tm_min) * 60 + int(t.tm_sec)
            begin_sec = int(begin_time) * 3600
            if now_sec - begin_sec > 0:
                se = int(hour) * 3600
                se_salary = money / int(data) / se
                get_moneys = se_salary * (now_sec - begin_sec)
                now_time = time.strftime('%H:%M:%S', time.localtime())
                if over_time == now_time:
                    return HttpResponse('下班')
                time.sleep(1)
                return HttpResponse('装逼王您今天赚了', round(get_moneys, 2))


def count_down_work(request):
    pass
