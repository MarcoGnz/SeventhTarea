
class Item:
    from ownable import set_owner
    # Lista para almacenar todas las instancias de Item creadas
    instances = []

    # Constructor de la clase Item
    def __init__(self, name, price, owner=None):
        # Inicializar atributos name, price y owner
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Almacenar la instancia actual en la lista de instancias
        Item.instances.append(self)

    # Método para obtener una etiqueta del Item (diccionario con name y price)
    def label(self):
        return {"name": self.name, "price": self.price}

    # Método estático para obtener todas las instancias de Item creadas
    @staticmethod
    def item_all():
        # Devolver la lista de instancias
        return Item.instances
