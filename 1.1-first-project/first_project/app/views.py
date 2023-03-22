import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.core.paginator import Paginator


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    workdir_request = os.listdir()
    return HttpResponse(workdir_request)
    # raise NotImplemented
def hello(request):
    context = {
        'test':5,
        'data': [1,5,8],
        'val': "hello",
    }
    return render(request, 'demo.html', context)

def sum(request, a, b):
    result = a + b
    return HttpResponse(f'Sum = {result}')

CONTENT = [str(i) for i in range(10000)]
def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)