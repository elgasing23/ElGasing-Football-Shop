from django.shortcuts import render, redirect, get_object_or_404
from main.models import Item
from main.forms import ItemForm
from django.http import HttpResponse
from django.core import serializers

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


def show_xml(request):
    Item_list = Item.objects.all()
    xml_data = serializers.serialize("xml", Item_list)
    return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    Item_list = Item.objects.all()
    json_data = serializers.serialize("json", Item_list)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, news_id):
   try:
       Item_item = Item.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", Item_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Item.DoesNotExist:
       return HttpResponse(status=404)
   
   
def show_json_by_id(request, news_id):
   try:
       Item_item = Item.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [Item_item])
       return HttpResponse(json_data, content_type="application/json")
   except Item.DoesNotExist:
       return HttpResponse(status=404)