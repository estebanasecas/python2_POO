# Realizar un programa que tenga una clase Persona con las siguientes caracteristicas. La clase tendra como atributos
#   el nombre y la edad de una persona. Implementar los metodos necesarios para inicializar los atributos, mostrar los datos 
#   e indicar si la persona es mayor de edad o no.

class Persona(object):

    def __init__(self):

        print('\nEste pograma determina la mayoria de edad.')

        self.nombre = input('\nNombre: ')

        while True:

            try:
            
                self.edad = int(input('Edad: '))
                break

            except ValueError:

                print("\nDebe ingresar un numero entero.")

    def mostrarDatos(self):

        print("\nSu nombre es %s." % self.nombre)
        print("Su edad es %d anos." % self.edad)

    def mayoriaEdad(self):

        if self.edad >= 18:
            print("\n%s es mayor de edad." % self.nombre)

        else:
            print("\n%s no es mayor de edad." % self.nombre)


inicio = Persona()

inicio.mostrarDatos()
inicio.mayoriaEdad()


     
