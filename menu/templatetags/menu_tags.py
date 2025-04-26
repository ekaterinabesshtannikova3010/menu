from django import template
from django.template.loader import render_to_string

from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    menu_items = MenuItem.objects.filter(parent=None)  # Получаем корневые элементы меню
    return render_to_string('menu/menu.html', {'menu_items': menu_items, 'current_path': current_path})
