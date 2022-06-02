from django.shortcuts import render

from pages.models import ArtWork

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {
        'featured': ArtWork.objects.filter(featured=True)
    }
    return render(request, 'home.html', context)


def about_view(request):
    context = {}
    return render(request, 'about.html', context)


def commissions_view(request):
    context = {}
    return render(request, 'commissions.html', context)
