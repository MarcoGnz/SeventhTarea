# Incluir este módulo le permitirá manipular sus propias instancias de elementos.

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Devuelve todas las instancias de Item propiedad del usuario.
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Devuelve la cantidad especificada de instancias de elementos que posee y que corresponden al número.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Muestra el estado del inventario de la instancia del artículo que posee en un formato de tabla con las columnas ["Número", "Nombre del producto", "Cantidad", "Cantidad"].
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["No.", "Nombre del producto", "Cantidad", "Cantidad"], tablefmt="grid"))    # Resultados de salida en formato de tabla utilizando el módulo de tabulación

def _stock(self):   # Devuelve el estado del inventario de la instancia del artículo que posee.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Ordene por instancias de elementos que devuelvan el mismo valor en el nombre del elemento.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # Tiendas de artículos clasificados Instancias de artículos.
    return stock
