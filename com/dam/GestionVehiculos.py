


class GestionVehiculos:
    def alta(self):
        print()

    def baja(self):
        print()

    def modificar(self):
        print()

    def buscar(self):
        print()

    def mostrar(self):
        print()
    def menu(self):
        salir = True
        while (salir):
            opc = input(
                "\t****GESTION VEHICULOS****\n 1. Alta\n 2. Baja\n 3. Modificar\n 4. Buscar \n 5. Mostrar todos\n 0. Salir\n ")
            if opc == "1":
                self.alta()
            elif opc == "2":
                self.baja()
            elif opc == "3":
                self.modificar()
            elif opc == "4":
                self.buscar()
            elif opc == "5":
                self.mostrar()
            elif opc == "0":
                print("Saliendo...")
                salir = False
            else:
                print("Esa opcion no existe")


