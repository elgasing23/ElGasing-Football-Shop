from django.urls import path
from main.views import (
    show_main,
    create_items,
    show_items,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user,
    edit_item,
    delete_item,
    items_collection,
    create_item_ajax,
    update_item_ajax,
    delete_item_ajax,
    item_stats,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-items/', create_items, name='create_items'),
    path('items/<str:id>/', show_items, name='show_items'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('api/items/', items_collection, name='items_collection'),
    path('api/items/create/', create_item_ajax, name='create_item_ajax'),
    path('api/items/<uuid:id>/update/', update_item_ajax, name='update_item_ajax'),
    path('api/items/<uuid:id>/delete/', delete_item_ajax, name='delete_item_ajax'),
    path('api/items/stats/', item_stats, name='item_stats'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('items/<uuid:id>/edit', edit_item, name='edit_item'),
    path('items/<uuid:id>/delete', delete_item, name='delete_item'),

    

]