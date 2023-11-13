
class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente. Transacción cancelada.")
            return

        # Transferir el precio de compra de todos los artículos del carrito al monedero del propietario del artículo
        for item in self.items:
            withdrawn_amount = self.owner.wallet.withdraw(item.price)

            if withdrawn_amount is not None:
                item.owner.wallet.deposit(withdrawn_amount)
                item.owner = self.owner

        # Vaciar el contenido del carrito
        self.items = []

        print("Compra realizada con éxito.")# - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner =?)
        
        