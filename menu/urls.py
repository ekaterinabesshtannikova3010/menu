from django.urls import path

from menu.apps import MenuConfig
from menu.views import tree_menu_view

app_name = MenuConfig.name

urlpatterns = [
    path('menu/', tree_menu_view, name='tree_menu'),
]
