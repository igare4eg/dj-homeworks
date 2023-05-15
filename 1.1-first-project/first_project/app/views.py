import datetime
import os
import random

from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.core.paginator import Paginator
from app.models import Car, Person



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

def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'M3']),
        color=random.choice(['C1', 'C2', 'C3'])
    )
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')

def list_car(request):
    car_objects = Car.objects.all()
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person(name='P', car=car).save()
        Person.objects.create(name='P', car=car)
    return HttpResponse('Все получилось')

def list_person(request):
    person_objects = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))