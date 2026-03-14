class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email

    def login(self):
        print(f"-------------------Inicio de seción---------------------")
        print (f"{self.nombre} ha iniciado seción")

    def actualizarPerfil(self,nuevoNombre, nuevoEmail):
        self.nombre = nuevoNombre
        self.email = nuevoEmail
        print(f"--------------Datos actualizados----------------------------------")
        print(f"ID: {self.idPersona}  Nombre: {self.nombre}  Email: {self.email}")

class Cliente(Persona):
    def __init__(self,idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)
        self.puntos=0
        self.historial=[]
        self.lista=[]

    def realizar_pedido(self,producto):
        self.lista.append(producto)
        self.historial.append(producto)
        self.puntos += int(producto.precioBase * 0.1)
        print(f"----------------Productos agregados---------------------------")
        print(f"El producto {producto.nombre} se agrego correctamente ")

    def consultar_Historial(self):
        print(f"-------------------Historial----------------------------------")
        print(f"Historial de {self.nombre}")
        for n in self.historial:
            print(f" {n.nombre} ${n.precioBase}")

    def canjear_Puntos(self):
        descuento=self.puntos
        print(f"-------------------Puntos---------------------")
        print(f"Tus puntos te han dado un descuento de {descuento}%")
        self.puntos=0

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, rol, idEmpleado):
        super().__init__(idPersona, nombre,email)
        self.rol=rol
        self.idEmpleado=idEmpleado

    def actualizar_inventario(self, NombreProducto, cantidad):
        print(f"-------------------Inventario Actualizado---------------------")
        print(f"se agregaron {cantidad} unidades a {NombreProducto}")

    def cambiar_Estado_Pedido(self,idPedido, idPedidoNuevo):
        print(f"-------------------Pedido actualizado---------------------")
        print(f"El pedio {idPedido} se ha cambiado a {idPedidoNuevo}")

class Productos():
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase
    
class Bebida(Productos):
    def __init__(self, idProducto, nombre, precioBase,tamaño,temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]

    def agregar_Extra(self,extra):
        self.modificadores.append(extra)

    def calcular_PrecioF(self):
        print(f"----------Precio Base---------------")
        return self.precioBase
    
class Postre(Productos):
    def __init__(self, idProducto, nombre, precioBase,esVegano,sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

class Pedido():
    def __init__(self,idPedido):
        self.idPedido=idPedido
        self.productos=[]
        self.estado="pendiente"
        self.total=0
    
    def calcular_Total(self):
        suma=0
        for p in self.productos:
            suma=suma+p.precioBase
        self.total=suma
        print("--------------Total-----------------------")
        return self.total
    
    def validar_Stock():
        return True
    
class Inventario():
    def __init__(self):
        self.ingredientes=[]

    def reducir_Stock(self,ingrediente,cantidad):
        print(f"El stock se redujo")

    def noticar_Faltante(self):
        print("bajo stock")