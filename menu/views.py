from django.shortcuts import render

from menu.models import MenuItem


def tree_menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'tree_menu.html', {'menu_items': menu_items})
