from django.shortcuts import render
from .models import Item

def show_main(request):
    context = {
        'npm' : '2406361694',
        'name': 'M Naufal Zhafran Rabiul Batara',
        'class': 'PBP F',
        'nama_project': 'ElGasing Football Shop',
    }
    return render(request, 'main.html', context)