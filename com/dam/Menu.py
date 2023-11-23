import GestionVehiculos
import GestionAlquiler
print("=================================")
salir = True
gesVehi = GestionVehiculos
gesAlq = GestionAlquiler
while(salir):
    opc = input("\t\t==== MENU ====\n 1. Gestion de Vehiculos\n 2. Gestion de Alquiler\n 0. Salir\n")
    if opc == "1":
        gesVehi.menu()

    elif opc == "2":
        gesAlq.menu()

    elif opc == "0":
        salir = False


print("Finalizamos Gestion de Alquileres")
