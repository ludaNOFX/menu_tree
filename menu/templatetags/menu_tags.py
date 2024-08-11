from typing import Optional, Dict, List

from menu.models import MenuItem
from menu.models.menu import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name: Optional[str] = None, menu_item: Optional[str] = None) ->\
        dict[str, list[MenuItem]] | dict[str, list[MenuItem]]:
    def get_menu(menu_item: Optional[str] = None, submenu: list = None) -> list[MenuItem]:
        menu: list[None] | list[MenuItem] = list(items.filter(parent=None)) if menu_item is None \
            else list(items.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)
    return {'menu': get_menu()} if menu_name == menu_item \
        else {'menu': get_menu(menu_item)}
