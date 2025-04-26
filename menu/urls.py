from django.urls import path

from menu.apps import MenuConfig
from menu.views import TreeMenuView

app_name = MenuConfig.name

urlpatterns = [
    path('', TreeMenuView.as_view(), name='tree_menu')
    # path('', tree_menu_view, name='tree_menu'),
]
