#Clase Padre
class Animal:
    def __init__(self, nombre, color, patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido(self):
        print("sonido generico")

class conejo(Animal):
    def sonido2(self):
        print(f"Snif Snif")
    def caract(self):
        print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas} patas")

class ornitorrinco(Animal):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas):
        self.pico=pico
    def sonido3(self):
        print("Grrrrrr")
    def caract1():
        print(f"Mi ornitorrinco se llama {self.nombre}")