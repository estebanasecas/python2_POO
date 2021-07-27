# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el telefono y el email.
# Ademas debera mostrar un menu con las siguientes opciones

# Anadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Borrar contacto
# Cerrar agenda

class Agenda(object):

    def __init__(self):

        print("\n********************")
        print("*Agenda electronica*")
        print("********************")

        self.agenda = {}

    def menu(self):    #------------------------------------------------------------------------------------------  menu                                                       

        while True:
         
            print("\n-MENU DE OPCIONES-")
            print("\n1.Anadir contacto.")
            print("2.Lista de contactos.")
            print("3.Buscar contacto.")
            print("4.Editar contacto.")
            print("5.Borrar contacto.")
            print("6.Cerrar agenda.")
        
            self.opcion = input("\nSeleccione una opcion: ")

            if self.opcion == '1':
                self.anadir()
                break

            elif self.opcion == '2':
                self.lista()
                break

            elif self.opcion == '3':
                self.buscar()
                break

            elif self.opcion == '4':
                self.editar()
                break

            elif self.opcion == '5':
                self.borrar()
                break

            elif self.opcion == '6':
                self.cerrar()
                break

            else:
                print("\nLa opcion ingresada no existe. Intente nuevamente.")
   
    def anadir(self):    #----------------------------------------------------------------------------------------- anadir

        print("\n---------------------------------") 
        print("\n1.ANADIR CONTACTO\n")

        self.nombre = input('Ingrese nombre: ')

        if self.agenda.get(self.nombre) == None:    # si no encuentra el index toma datos

            self.toma_datos()                       

        else:

            print("\nEse contacto ya existe. Se va a sobreescibir.")
            continuar = input("\nDesea continuar (s / n) ")

            if continuar == 's':
        
                print("")
                self.toma_datos()    
                                
            else:

                print("\nSu contacto no se a anadido.")

        print("\n---------------------------------")
        self.menu()


    def toma_datos(self):    #--------------------------------------------- sub toma datos (anadir)

        telefono = input('Ingrese telefono: ')
        email = input('Ingrese email: ')

        datos = [telefono, email]
        
        self.agenda[self.nombre]= datos                         

        print("\nSu nuevo contacto se a anadido.")


    def lista(self):    #------------------------------------------------------------------------------------------ lista

        print("\n---------------------------------")
        print("\n2.LISTA DE CONTACTOS\n")

        self.contador = 1

        for nombre, datos in self.agenda.items():
 
            print("  %d. %s / %s / %s" % (self.contador, nombre, datos[0], datos[1]))

            self.contador += 1

        print("\n---------------------------------")

        self.menu()

    def buscar(self):    #----------------------------------------------------------------------------------------- buscar

        print("\n---------------------------------")
        print("\n3.BUSCAR CONTACTO")

        busqueda = input("\nIngrese contacto que desea buscar: ")

        if self.agenda.get(busqueda):                                 # get() function  > True / None 

            print('\n  %s / %s / %s' % (busqueda, (self.agenda[busqueda])[0], (self.agenda[busqueda])[1]))

        else:

            print("\nEl contacto no se encuentra registrado.")

        print("\n---------------------------------")

        self.menu()

    def editar(self):    #----------------------------------------------------------------------------------------- editar

        print("\n---------------------------------")
        print("\n4.EDITAR CONTACTO")

        busqueda = input('\nIngrese contacto que desea editar: ')

        if self.agenda.get(busqueda):

            print('\n  %s / %s / %s' % (busqueda, (self.agenda[busqueda])[0], (self.agenda[busqueda])[1]))

            editTelefono = input("\n  Ingrese nuevo telefono: ")
            editMail = input("  Ingrese nuevo mail: ")

            editDatos = [editTelefono, editMail]

            self.agenda[busqueda] = editDatos

            print('\nEl contacto ha sido editado exitosamente.')  

            print('\n  %s / %s / %s' % (busqueda, (self.agenda[busqueda])[0], (self.agenda[busqueda])[1]))

        else:
        
            print("\nEl contacto no se encuentra registrado.")

        print("\n---------------------------------")

        self.menu()

    def borrar(self):    #----------------------------------------------------------------------------------------- borrar

        print("\n---------------------------------")
        print("\n5.BORRAR CONTACTO")

        busqueda = input('\nIngrese contacto que desea borrar: ')

        if self.agenda.get(busqueda):

            print("\n  %s / %s / %s" % (busqueda, (self.agenda[busqueda])[0], (self.agenda[busqueda])[1]))

            while True:

                esta_seguro = input("\nEsta seguro que desea borrar el contacto (s / n): ")            

                if esta_seguro == 's':

                    self.agenda.pop(busqueda)
                    print("\nEl contacto ha sido borrado exitosamente.")
                    break

                elif esta_seguro == 'n':

                    print("\nEl contacto no ha sido borrado.")             
                    break

                else:
                    
                    print("\nLa opcion ingresada no existe. Intente nuevamente.")         
     
        else:
        
            print("\nEl contacto no se encuentra registrado.")

        print("\n---------------------------------")

        self.menu()

    def cerrar(self):    #----------------------------------------------------------------------------------------- cerrar

        print("\nHasta la proxima!")
        exit(0)



inicio = Agenda()

inicio.menu()








