import GestionVehiculos
import GestionAlquiler
print("Iniciamos Gestion de Alquileres")
salir = True
gesVehi = GestionVehiculos.GestionVehiculos()
gesAlq = GestionAlquiler
while(salir):
    opc = input("\t\t****MENU****\n 1. Gestion de Vehiculos\n 2. Gestion de Alquiler\n 0. Salir\n")
    if opc == "1":
        print("Aqui Gestion de Vehiculos")
        gesVehi.menu()
    elif opc == "2":
        print("Aqui Gestion de Alquiler")
        gesAlq.menu()
    elif opc == "0":
        print("Saliendo...")
        salir = False


print("Finalizamos Gestion de Alquileres")
