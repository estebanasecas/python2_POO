# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
#   Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y 
#   si ha aprobado o no.

class Alumno(object):

    def __init__(self):

        print '\n***Sistema de promedio del alumno***\n'

        self.nombre = raw_input('Nombre del alumno: ')

        while True:

            try:
            
                self.matematicas = float(raw_input('\nNota Matematicas: '))
                self.biologia = float(raw_input('Nota Biologia: '))
                self.lenguaje = float(raw_input('Nota Lenguaje: '))
                self.social = float(raw_input('Nota Ed.Social: '))
                self.catequesis = float(raw_input('Nota Catequesis: '))
                break

            except ValueError:

                print '\nDebe ingresar solo numeros. Intente nuevamente.'

    def promedio(self):

        self.promedio = (self.matematicas + self.biologia + self.lenguaje +
                         self.social + self.catequesis) / 5

    def resultado(self):

        print '\nEl promedio de %s es %.2f' % (self.nombre, self.promedio)

        if self.promedio >= 6:

            print '\nEl/la alumno/a %s a aprobado el curso.' % self.nombre
        else:
            print '\nEl/la alumno/a %s no a aprobado el curso.' % self.nombre


promediador = Alumno()

promediador.promedio()
promediador.resultado()












