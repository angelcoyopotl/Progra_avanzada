from café import *



prod1 = Bebida(112, "Café americano", 30, "pequeño", "Caliente")
prod2 = Bebida(113, "Capuchino vainilla", 45,"mediano", "Caliente")
prod3 = Bebida(114, "Latte macchiato", 48,"grande", "frio")
prod4 = Bebida(115, "Espresso doble", 35, "pequeño", "Caliente")
prod5 = Bebida(116, "Mocaccino frío", 52, "grande", "frio")
prod6 = Bebida(117, "Té verde matcha", 50, "mediano", "frio")
prod7 = Bebida(118, "Chocolate caliente", 40, "mediano", "Caliente")

prod8 = Postre(119, "Croissant de mantequilla", 35, "No", "no")
prod9 = Postre(120, "Muffin de arándanos", 38, "No", "si")
prod10 = Postre(121, "Bagel con crema", 42, "No", "si")

cliente1=Cliente(1234, "Angel Coyopotl", "coyopotlangel@gmail.com")

empleado1=Empleado(132,"Sandra", "sandramar@gmail.com", "Barista", 1)

inventario = Inventario()
pedido = Pedido(5001)
cliente1.login()
cliente1.actualizarPerfil("Tilin","Tilin2.0@gmail.com")
empleado1.actualizar_inventario("Granos de Café", 50)
empleado1.cambiar_Estado_Pedido(112, 115)
cliente1.realizar_pedido(prod1)
cliente1.realizar_pedido(prod8)
cliente1.consultar_Historial()
prod3.agregar_Extra("Leche de Almendras")
prod3.agregar_Extra("Jarabe de Vainilla")
precio_bebida = prod3.calcular_PrecioF()
prod7.agregar_Extra(extra="Extra Chocolate")
print(f"Extras en {prod3.nombre} {prod3.modificadores}")
print(f"Precio final confirmado ${precio_bebida}")
pedido.productos.append(prod1)
pedido.productos.append(prod8)
if Pedido.validar_Stock():
    total_compra = pedido.calcular_Total()
    print(f"El total a pagar del pedido {pedido.idPedido} es: ${total_compra}")
    pedido.estado = "Pagado"
inventario.ingredientes = ["Leche", "Granos de Café", "Azúcar"]
print(f"----------------------- Movimiento de Inventario --------------------")
inventario.reducir_Stock("Leche", 1)
inventario.noticar_Faltante()
cliente1.canjear_Puntos()