from django.shortcuts import render, redirect, get_object_or_404
from main.models import Item
from main.forms import ItemForm
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        item_list = Item.objects.all()
    else:
        item_list = Item.objects.filter(user=request.user)
    
    context = {
        'npm' : '2406361694',
        'name': 'M Naufal Zhafran Rabiul Batara',
        'class': 'PBP F',
        'nama_project': 'ElGasing Football Shop',
        'item_list': item_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form_entry = form.save(commit = False)
        form_entry.user = request.user
        form_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)


@login_required(login_url='/login')
def show_items(request, id):
    item = get_object_or_404(Item, pk=id)
    item.increment_views()

    context = {
        'item': item
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
   
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_items.html", context)


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))