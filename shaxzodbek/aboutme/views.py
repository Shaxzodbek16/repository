from django.shortcuts import render
from .models import Information, Wish


def mainpage(request):
    return render(request, 'mainpage.html')


def all_info(request):
    info = Information.objects.all().order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'all_info.css',
        'title': 'All information'
    }
    return render(request, 'index.html', context=context)


def aboutme(request):
    info = Information.objects.filter(category="aboutme").order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'aboutme.css',
        'title': 'About me'
    }
    return render(request, 'index.html', context=context)


def love(request):
    info = Information.objects.filter(category="love").order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'love.css',
        'title': 'About love'
    }
    return render(request, 'index.html', context=context)


def friends(request):
    info = Information.objects.filter(category="friends").order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'friends.css',
        'title': 'About friends'
    }
    return render(request, 'index.html', context=context)


def family(request):
    info = Information.objects.filter(category="family").order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'family.css',
        'title': 'About family'
    }
    return render(request, 'index.html', context=context)


def projects(request):
    info = Information.objects.filter(category="projects").order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'all_info.html',
        'css_name': 'projects.css',
        'title': 'About projects'
    }
    return render(request, 'index.html', context=context)


def wish(request):
    info = Wish.objects.all().order_by('-date_created')
    context = {
        'info': info,
        'html_name': 'wish.html',
        'css_name': 'wish.css',
        'title': 'About wish'
    }
    return render(request, 'index.html', context=context)


def _404(request):
    return render(request, '404.html.html', status=404)
