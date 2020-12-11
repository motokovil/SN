
class Empleado:

    def __init__(self, sueldo):
        self.sueldo = sueldo
    def prestamo(self, valor):
        if valor > self.sueldo:
            raise ValueError("No cumple con las condiciones")
        else:
            return True