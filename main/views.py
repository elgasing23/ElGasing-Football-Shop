from django.shortcuts import render, get_object_or_404
from main.models import Item
from main.forms import ItemForm
import datetime
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie


def _serialize_item(item, user=None):
    """Serialize an Item instance for JSON responses."""
    current_user_id = getattr(user, "id", None)
    return {
        "id": str(item.id),
        "name": item.name,
        "price": item.price,
        "description": item.description,
        "thumbnail": item.thumbnail,
        "category": item.category,
        "category_display": item.get_category_display(),
        "is_featured": item.is_featured,
        "items_views": item.items_views,
        "owner": item.user.username if item.user else None,
        "is_owner": current_user_id is not None and item.user_id == current_user_id,
        "detail_url": reverse("main:show_items", args=[item.id]),
    }


@ensure_csrf_cookie
@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm': '2406361694',
        'name': 'M Naufal Zhafran Rabiul Batara',
        'class': 'PBP F',
        'nama_project': 'ElGasing Football Shop',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, 'main.html', context)


@login_required(login_url='/login')
def item_list_ajax(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        items = Item.objects.filter(user=request.user)
    else:
        items = Item.objects.all()

    data = [_serialize_item(item, request.user) for item in items]
    return JsonResponse({"items": data})


@login_required(login_url='/login')
@require_POST
def create_items(request):
    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "errors": {"__all__": ["Invalid JSON payload."]}}, status=400)

    form = ItemForm(payload)

    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return JsonResponse({
            "success": True,
            "item": _serialize_item(item, request.user)
        }, status=201)

    return JsonResponse({"success": False, "errors": form.errors}, status=400)


@login_required(login_url='/login')
@require_http_methods(["PUT"])
def edit_item(request, id):
    item = Item.objects.filter(pk=id).first()
    if not item:
        return JsonResponse({"success": False, "errors": {"__all__": ["Item not found."]}}, status=404)

    if item.user_id != request.user.id:
        return JsonResponse({"success": False, "errors": {"__all__": ["You are not allowed to edit this item."]}}, status=403)

    try:
        payload = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "errors": {"__all__": ["Invalid JSON payload."]}}, status=400)

    form = ItemForm(payload, instance=item)
    if form.is_valid():
        item = form.save()
        return JsonResponse({"success": True, "item": _serialize_item(item, request.user)})

    return JsonResponse({"success": False, "errors": form.errors}, status=400)


@login_required(login_url='/login')
@require_http_methods(["DELETE"])
def delete_item(request, id):
    item = Item.objects.filter(pk=id).first()
    if not item:
        return JsonResponse({"success": False, "errors": {"__all__": ["Item not found."]}}, status=404)

    if item.user_id != request.user.id:
        return JsonResponse({"success": False, "errors": {"__all__": ["You are not allowed to delete this item."]}}, status=403)

    item.delete()
    return JsonResponse({"success": True})


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
   
   
@ensure_csrf_cookie
def register(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "errors": {"__all__": ["Invalid JSON payload."]}}, status=400)

        form = UserCreationForm(payload)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success": True,
                "redirect_url": reverse('main:login')
            }, status=201)

        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    return render(request, 'register.html')


@ensure_csrf_cookie
def login_user(request):
   if request.method == 'POST':
      try:
          payload = json.loads(request.body or "{}")
      except json.JSONDecodeError:
          return JsonResponse({"success": False, "errors": {"__all__": ["Invalid JSON payload."]}}, status=400)

      form = AuthenticationForm(request, data=payload)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({
            "success": True,
            "redirect_url": reverse("main:show_main")
        })
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

      errors = form.errors if form.errors else {"__all__": ["Invalid credentials."]}
      return JsonResponse({"success": False, "errors": errors}, status=400)

   return render(request, 'login.html')


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
