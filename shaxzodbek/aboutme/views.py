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
    # return only love.html info from catagory filter


def friends(request):
    pass
    # return only friends info from catagory filter


def family(request):
    pass
    # return only family info from catagory filter


def projects(request):
    pass
    # return only projects.html info from catagory filter


def wish(request):
    pass
    # return only wishes info from catagory filter


def _404(request):
    return render(request, '404.html.html', status=404)
