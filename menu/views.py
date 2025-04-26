# from django.shortcuts import render
#
# from menu.models import MenuItem
#
#
# def tree_menu_view(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, 'menu/tree_menu.html', {'menu_items': menu_items})
from django.views import View
from django.shortcuts import render
from menu.models import MenuItem


class TreeMenuView(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        return render(request, 'menu/menu.html', {'menu_items': menu_items})
