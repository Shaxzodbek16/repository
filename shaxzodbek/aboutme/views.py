from django.shortcuts import render
from .models import Information


def mainpage(request):
    return render(request, 'mainpage.html')


def all_info(request):
    contest = {
        "information": Information.objects.all(),
    }
