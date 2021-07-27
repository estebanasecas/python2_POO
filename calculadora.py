# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el metodo __init__.
#   Calcular despues la suma, resta, multiplicacion y division. Utilizar un metodo para cada una e imprimir los resultados obtenidos.
#   Llamar a la clase Calculadora.

class Calculadora(object):

    def __init__(self):

        print("\n***Este programa realiza y muestra las cuatro operaciones entre dos numeros enteros***")

        while True:

            try:

                self.valorUno = int(input("\nIngrese valor uno: "))
                self.valorDos = int(input("Ingrese valor dos: "))
                break

            except ValueError:

                print("\nDebe ingresar un numero entero. Intente nuevamente.")

    def suma(self):

        self.suma = self.valorUno + self.valorDos

        print("\nLa suma de %d y %d es %d." % (self.valorUno, self.valorDos, self.suma))

    def resta(self):

        self.resta = self.valorUno - self.valorDos

        print("La resta entre %d y %d es %d." % (self.valorUno, self.valorDos, self.resta))

    def multiplicacion(self):

        self.multiplicacion = self.valorUno * self.valorDos

        print("La multiplicacion entre %d y %d es %d." % (self.valorUno, self.valorDos, self.multiplicacion))

    def division(self):

        try:       
            self.division = float(self.valorUno) / float(self.valorDos)       
            print("La division de %d entre %d es %.2f." % (self.valorUno, self.valorDos, self.division))

        except ZeroDivisionError:
            print("No se puede dividir un por 0.")

inicio = Calculadora()

inicio.suma()
inicio.resta()
inicio.multiplicacion()
inicio.division()

        
















