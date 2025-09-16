from django.shortcuts import render, redirect, get_object_or_404
from main.models import Item
from main.forms import ItemForm

def show_main(request):
    item_list = Item.objects.all()
    
    context = {
        'npm' : '2406361694',
        'name': 'M Naufal Zhafran Rabiul Batara',
        'class': 'PBP F',
        'nama_project': 'ElGasing Football Shop',
        'item_list': item_list
    }
    return render(request, 'main.html', context)

def create_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)

def show_items(request, id):
    items = get_object_or_404(Item, pk=id)
    items.increment_views()

    context = {
        'items': items
    }

    return render(request, "items_detail.html", context)