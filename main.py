class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = 0

    def cantidadAsientos(self):
        count = 0
        for i in self.asientos:
            if i != None:
                count += 1
        return count
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for i in range(len(self.asientos)):
            if self.asientos[i] != None and self.asientos[i].registro != self.registro:
                return "Las piezas no son originales"
        return "Auto original"


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color.lower() in coloresPermitidos:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tiposPermitidos =  ["electrico", "gasolina"]
        if tipo.lower() in tiposPermitidos:
            self.tipo = tipo
