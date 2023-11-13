# Importar las clases Customer, Item y Seller desde sus respectivos módulos
from customer import Customer
from item import Item
from seller import Seller

# Crear una instancia de Seller (vendedor) con el nombre "DIC tienda"
seller = Seller("DIC tienda")

# Generar 10 artículos para el vendedor (Seller)
for i in range(10):
    Item("CPU", 40830, seller)
    Item("memoria", 13880, seller)
    Item("placa base", 28980, seller)
    Item("unidad fuente de alimentacion", 8980, seller)
    Item("Caja de PC", 8727, seller)
    Item("3.5 pulgadas de HDD", 10980, seller)
    Item("2.5 pulgadas de SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU cooler", 13400, seller)
    Item("tablero grafico", 23800, seller)

# Solicitar al usuario su nombre y crear una instancia de Customer (cliente) con ese nombre
print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

# Solicitar al usuario cargar dinero en su billetera y realizar el depósito
print("🏧 Por favor, ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

# Iniciar el proceso de compra
print("🛍️ Empieza a comprar")
end_shopping = False
while not end_shopping:
    # Mostrar la lista de productos disponibles
    print("📜 Lista de productos")
    seller.show_items()

    # Solicitar al usuario el número y la cantidad de productos a comprar
    print("️️⛏ Por favor, ingrese el número de producto")
    number = int(input())
    print("⛏ Por favor, ingrese la cantidad del producto")
    quantity = int(input())

    # Seleccionar los artículos del vendedor y agregarlos al carrito del cliente
    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)

    # Mostrar el contenido actual del carrito y el total
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Cantidad total: {customer.cart.total_amount()}")

    # Preguntar al usuario si desea terminar de comprar
    print("😭 ¿Quieres terminar de comprar? (yes/no)")
    end_shopping = input() == "yes"

# Preguntar al usuario si desea confirmar la compra y realizar el proceso de check-out si es el caso
print("💸 ¿Quieres confirmar tu compra? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

# Mostrar resultados finales: propiedad del cliente, saldo de su billetera, estado del inventario del vendedor y su saldo de billetera, contenido final del carrito y su cantidad total
print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultado ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name} propiedades:")
customer.show_items()
print(f"😱👛 {customer.name} saldo de billetera: {customer.wallet.balance}")

print(f"📦 {seller.name} estado del inventario:")
seller.show_items()
print(f"😻👛 {seller.name} saldo de billetera: {seller.wallet.balance}")

print("🛒 Contenido final del carrito")
customer.cart.show_items()
print(f"🌚 Cantidad total: {customer.cart.total_amount()}")

print("🎉 Fin")