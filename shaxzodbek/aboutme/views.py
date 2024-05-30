from django.shortcuts import render
from .models import Information


def mainpage(request):
    return render(request, 'mainpage.html')


def all_info(request):
    pass
    # return all information about me


def aboutme(request):
    pass
    # return only mine info from catagory filter


def love(request):
    pass
    # return only love info from catagory filter


def friends(request):
    pass
    # return only friends info from catagory filter


def family(request):
    pass
    # return only family info from catagory filter


def projects(request):
    pass
    # return only projects info from catagory filter
