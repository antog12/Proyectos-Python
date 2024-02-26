class Persona:

    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance # balance es el saldo que tiene en su cuenta

    def __str__(self):
        self.nombre
        self.apellido
        self.numero_cuenta
        self.balance

        return f"El cliente {self.nombre} {self.apellido} con múmero de cuenta {self.numero_cuenta} tiene en su cuenta {self.balance} euros"

    def depositar(self,cantidad):
        self.balance=self.balance + cantidad
        return self.balance

    def retirar(self,cantidad):
        if cantidad <= self.balance:
            self.balance=self.balance-cantidad
        else:
            print("Saldo insuficiente")
        return self.balance




cliente1=Cliente(nombre=input("Nombre: "),apellido=input("Apellido: "),numero_cuenta=input("Número de cuenta: "),balance=10000)
cliente2=Cliente("Candela","Abellán",4321,8000)
#cliente1.depositar(10000)
cliente1.retirar(5000)
print(cliente1)






