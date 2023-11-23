import VerificationExceptions
def alta():
    print();
def baja():
    print()
def modificar():
    print()
def buscar():
    print()
def mostrar():
    print()
def menu():
       salir = True
       while (salir):
           opc = input(
               "\t****GESTION ALQUILER****\n 1. Alta\n 2. Baja\n 3. Modificar\n 4. Buscar \n 5. Mostrar todos\n 0. Salir\n ")

           if opc == "1":
               alta()
           elif opc == "2":
               baja()
           elif opc == "3":
               modificar()
           elif opc == "4":
               buscar()
           elif opc == "5":
               mostrar()
           elif opc == "0":
               print("Saliendo...")
               salir = False
           else:
               print("Esa opcion no existe")
