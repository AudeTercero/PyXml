import xml.etree.ElementTree as ET
def leerVehiculos(xml):
    try:
        tree = ET.parse(xml)
        root = tree.getroot()

        vehiculosLista = []

        for vehiculo_element in root.findall('vehiculo'):
            vehiculoInfo = []

            # Extraer información de cada elemento dentro de vehiculo
            id = vehiculo_element.find('id').text
            matricula = vehiculo_element.find('matricula').text
            marca_modelo = vehiculo_element.find('marca_modelo').text
            anoFabricacion = vehiculo_element.find('ano_fabricacion').text
            tarifaDia = vehiculo_element.find('tarifa_por_dia').text
            estado = vehiculo_element.find('estado').text

            # Agregar la información del vehículo a la lista
            vehiculoInfo.extend([id, matricula, marca_modelo, anoFabricacion, tarifaDia, estado])

            vehiculosLista.append(vehiculoInfo)

        return vehiculosLista

    except FileNotFoundError:
        print(f"El archivo {xml} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo XML: {e}")
        return None


def leerAlquileres():
    print()


def aniadirVehiculo(matricula, marca, modelo, anio_fabricacion, tarifa_por_dia, estado):
    print(matricula, marca, modelo, anio_fabricacion, tarifa_por_dia, estado)


def aniadirAlquiler():
    print()

def eliminarVehiculo(matricula):
    print()

def eliminarAlquiler():
    print()


