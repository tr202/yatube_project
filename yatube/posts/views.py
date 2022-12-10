from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(' В путь!')


def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}.')
