import datetime
import json

from django.shortcuts import render, redirect, get_object_or_404
from main.models import Item
from main.forms import ItemForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string


def serialize_item(item: Item) -> dict:
    return {
        "id": str(item.id),
        "name": item.name,
        "price": item.price,
        "description": item.description,
        "category": item.category,
        "thumbnail": item.thumbnail,
        "is_featured": item.is_featured,
        "created_at": item.created_at.isoformat() if item.created_at else None,
        "items_views": item.items_views,
        "owner": item.user.username if item.user else None,
    }


@login_required(login_url='/login')
def show_main(request):
    context = {
        "npm": "2406361694",
        "name": "M Naufal Zhafran Rabiul Batara",
        "class": "PBP F",
        "nama_project": "ElGasing Football Shop",
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    return render(request, "main.html", context)

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


@login_required(login_url="/login")
def items_collection(request):
    filter_type = request.GET.get("filter", "all")
    queryset = Item.objects.all().order_by("-created_at")

    if filter_type == "my":
        queryset = queryset.filter(user=request.user)
    elif filter_type == "featured":
        queryset = queryset.filter(is_featured=True)

    data = [serialize_item(item) for item in queryset]
    html = "".join(
        render_to_string("card_item.html", {"item": item}, request=request)
        for item in queryset
    )

    return JsonResponse({"success": True, "data": data, "html": html})


@login_required(login_url="/login")
@require_http_methods(["POST"])
def create_item_ajax(request):
    if request.headers.get("x-requested-with") != "XMLHttpRequest":
        return JsonResponse({"success": False, "message": "AJAX request required."}, status=400)

    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Invalid JSON payload."}, status=400)

    if isinstance(payload.get("is_featured"), bool):
        payload["is_featured"] = "on" if payload["is_featured"] else ""

    form = ItemForm(payload)

    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return JsonResponse(
            {
                "success": True,
                "message": "Item created successfully.",
                "data": serialize_item(item),
            },
            status=201,
        )

    return JsonResponse({"success": False, "errors": form.errors}, status=400)


@login_required(login_url="/login")
@require_http_methods(["POST"])
def update_item_ajax(request, id):
    if request.headers.get("x-requested-with") != "XMLHttpRequest":
        return JsonResponse({"success": False, "message": "AJAX request required."}, status=400)

    item = get_object_or_404(Item, pk=id, user=request.user)

    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Invalid JSON payload."}, status=400)

    if isinstance(payload.get("is_featured"), bool):
        payload["is_featured"] = "on" if payload["is_featured"] else ""

    form = ItemForm(payload, instance=item)

    if form.is_valid():
        item = form.save()
        return JsonResponse(
            {
                "success": True,
                "message": "Item updated successfully.",
                "data": serialize_item(item),
            }
        )

    return JsonResponse({"success": False, "errors": form.errors}, status=400)


@login_required(login_url="/login")
@require_http_methods(["POST"])
def delete_item_ajax(request, id):
    if request.headers.get("x-requested-with") != "XMLHttpRequest":
        return JsonResponse({"success": False, "message": "AJAX request required."}, status=400)

    item = get_object_or_404(Item, pk=id, user=request.user)
    item.delete()
    return JsonResponse({"success": True, "message": "Item deleted successfully."})


@login_required(login_url="/login")
def item_stats(request):
    total_items = Item.objects.count()
    my_items = Item.objects.filter(user=request.user).count()
    featured_items = Item.objects.filter(is_featured=True).count()
    latest_item = Item.objects.filter(user=request.user).order_by("-created_at").first()
    most_viewed = Item.objects.order_by("-items_views").first()

    return JsonResponse(
        {
            "success": True,
            "data": {
                "total_items": total_items,
                "my_items": my_items,
                "featured_items": featured_items,
                "latest_item": serialize_item(latest_item) if latest_item else None,
                "most_viewed": serialize_item(most_viewed) if most_viewed else None,
            },
        }
    )


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

    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
            payload = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON payload."}, status=400)

        form = UserCreationForm(payload)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    "success": True,
                    "message": "Your account has been successfully created!",
                    "redirect_url": reverse("main:login"),
                },
                status=201,
            )

        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
            payload = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON payload."}, status=400)

        form = AuthenticationForm(request, data=payload)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse(
                {
                    "success": True,
                    "message": "Welcome back!",
                    "redirect_url": reverse("main:show_main"),
                }
            )
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        logout(request)
        response = JsonResponse(
            {
                "success": True,
                "message": "You have been signed out.",
                "redirect_url": reverse("main:login"),
            }
        )
        response.delete_cookie("last_login")
        return response

    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
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