import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from pathlib import Path
from datetime import datetime

from com.dam import VerificationExceptions


# ******************** FUNCIONES  VEHICULOS **************************************

def existe_matricula(fichero, matricula):
    """
    Funcion para comprobar si existe la matricula o no
    :param fichero: recibe el fichero
    :param matricula: recibe la matricula
    :return: retorna true o false segun si existe o no
    """
    if (Path(fichero).exists() is True):
        tree = ET.parse(fichero)
        root = tree.getroot()
        for elemento in root.iter('vehiculo'):
            mat_aux = elemento.find('matricula').text
            if (matricula == mat_aux):
                return True
    return False


def esta_disponible(fichero, matricula):
    if (Path(fichero).exists() is True):
        tree = ET.parse(fichero)
        root = tree.getroot()
        for elemento in root.iter('vehiculo'):
            mat_aux = elemento.find('matricula').text

            if (matricula == mat_aux):
                estado = elemento.find("estado").text

                if estado == "disponible":
                    return True
    return False


def obtener_atributos_vehiculo(xml_path, matricula):
    """
    Funcion para obntener un listado de con los atributos de un vehiculo
    :param xml_path: recibe le fichero
    :param matricula: recibe la matricula del vehiculo
    :return: retorna los atributos del vehiculo
    """
    atributos_vehiculo = []

    if Path(xml_path).exists():
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()

            for vehiculo in root.findall('vehiculo'):
                mat_vehi = vehiculo.find('matricula').text
                if (mat_vehi == matricula):
                    atributos_vehiculo.append(vehiculo.find("id").text)
                    atributos_vehiculo.append(vehiculo.find("matricula").text)
                    atributos_vehiculo.append(vehiculo.find("descripcion/marca").text)
                    atributos_vehiculo.append(vehiculo.find("descripcion/modelo").text)
                    atributos_vehiculo.append(vehiculo.find("id").text)
                    atributos_vehiculo.append(vehiculo.find("id").text)
                    atributos_vehiculo.append(vehiculo.find("estado").text)

        except FileNotFoundError:
            print("No hay vehiculos guardados")
        except Exception as e:
            print(f"Error: {e}")

    return atributos_vehiculo


def hay_vehiculos(xml_path):
    """
    Funcion para comprobar si hay vehiculos guardados
    :param xml_path: recibe el fichero
    :return: retorna true o false encaso de que encuentre vehiculos o no
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        if not root.findall("vehiculo"):
            print("No hay vehiculos guardados.")
            return False
        else:
            return True

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


def leer_vehiculos(xml_path):
    """
    Funcion para mostrar todos los vehiculos guardados
    :param xml_path: Recibe el fichero
    :return:
    """
    if Path(xml_path).exists():
        tree = ET.parse(xml_path)
        root = tree.getroot()

        if not root.findall('vehiculo'):
            print("No hay vehiculos guardados.")
        else:
            print("========== LISTADO VEHICULOS ==========")
            for elemento in root.iter('vehiculo'):
                id_vehiculo = elemento.get('id')
                matricula = elemento.find('matricula').text
                marca = elemento.find('descripcion/marca').text
                modelo = elemento.find('descripcion/modelo').text
                anio_fabricacion = elemento.find('anioFabricacion').text
                tarifa_dia = elemento.find('tarifaDia').text
                estado = elemento.find('estado').text

                print(f'''****VEHICULO****
Id: {id_vehiculo}
Matricula: {matricula}
Marca: {marca}
Modelo: {modelo}
Anio de Fabricacion: {anio_fabricacion}
Tarifa Diaria: {tarifa_dia}
Estado: {estado}        
***********************''')


def aniadir_vehiculo(matricula, marca, modelo, anio_fabricacion, tarifa_dia, estado, xml_path):
    """
    Funcion para guardar vehiculos
    :param matricula: recibe la matricula del vehiculo
    :param marca: recibe la marca del vehiculo
    :param modelo: recibe el modelo del vehiculo
    :param anio_fabricacion: recibe el anio de fabricacion
    :param tarifa_dia: recibe la tarifa por dia
    :param estado: recibe el estado del vehiculo
    :param xml_path: recibe el fichero
    :return:
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except FileNotFoundError:
        root = Element('vehiculos')
        tree = ET.ElementTree(root)

    # Creamos el vehiculo y su atributo
    vehiculo = ET.Element('vehiculo')
    vehiculo.set('id', str(obtId(xml_path, "vehiculo")))

    # Creamos sus atributos o subelementos
    ET.SubElement(vehiculo, 'matricula').text = matricula
    descripcion = ET.SubElement(vehiculo, 'descripcion')
    ET.SubElement(descripcion, 'marca').text = marca
    ET.SubElement(descripcion, 'modelo').text = modelo
    ET.SubElement(vehiculo, 'anioFabricacion').text = str(anio_fabricacion)
    ET.SubElement(vehiculo, 'tarifaDia').text = str(tarifa_dia)
    ET.SubElement(vehiculo, 'estado').text = estado

    # Agregamos el nuevo vehiculo
    root.append(vehiculo)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("vehiculos.xml", "w")
    file.write(salida)
    file.close()
    eliminarEspacios("vehiculos.xml")


def eliminar_vehiculo(matricula, xml_path):
    """
    Funcion para eliminar vehiculos guardados
    :param matricula: recibe la matricula del vehilo que queremos eliminar
    :param xml_path: recibe le fichero de vehiculos
    :return:
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text

            if (mat_vehi == matricula):
                root.remove(vehiculo)
                tree.write(xml_path)
                print("El vehiculo ha sido eliminado")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


def modificar_vehiculo(matricula, xml_path):
    """
    Funcion para modificar los vehiculos guardados
    :param matricula: recibe la matricula del vehiculo a modificar
    :param xml_path: recibe el fichero de vehiculos
    :return:
    """
    vehiculo_encontrado = False
    salir = False

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text

            if mat_vehi == matricula:
                vehiculo_encontrado = True
                id = vehiculo.get("id")

        # Si no lo encuentra, lo indicamos
        if not vehiculo_encontrado:
            print("No se encontro el vehiculo")
        else:
            while not salir:
                opc = input(
                    "\tSelecciona una opcion:\n 1. Modificar ID \n 2. Modificar Matricula\n 3. Modificar Marca\n 4. Modificar Modelo"
                    "\n 5. Modificar Anio de Fabricacion \n 6. Modificar Tarifa Diaria\n 7. Modificar estado "
                    "\n 0. Salir \n")

                # Hay que controlar que no se repitan id ni matricula
                if opc == "1":
                    id_valido = False

                    while not id_valido:
                        nuevo_id = input("Ingresa el nuevo ID del vehiculo")

                        try:
                            VerificationExceptions.esNum(nuevo_id)

                            if existe_id(xml_path, nuevo_id, "vehiculo") is not True:
                                id_valido = True
                                modificar_atributo(xml_path, "vehiculo", id, nuevo_id)
                            else:
                                print("El ID introducido ya pertenece a un vehiculo existente.")


                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "2":
                    mat_valida = False

                    while not mat_valida:
                        nueva_mat = input("Ingresa la nueva matricula del vehiculo")

                        try:
                            VerificationExceptions.hayAlgo(nueva_mat)
                            VerificationExceptions.matFormat(nueva_mat)

                            if existe_matricula(xml_path, nueva_mat) is not True:
                                mat_valida = True
                                modificar_etiqueta(xml_path, "vehiculo", "matricula", id, nueva_mat)
                            else:
                                print("La matricula introducida ya pertenece a un vehiculo existente.")

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "3":
                    mar_valida = False

                    while not mar_valida:
                        nuevaMarca = input("Ingrese la nueva marca del vehiculo: ")

                        try:
                            VerificationExceptions.hayAlgo(nuevaMarca)
                            modificar_etiqueta(xml_path, "vehiculo", "descripcion/marca",
                                               id, nuevaMarca)
                            mar_valida = True

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "4":
                    mod_valido = False

                    while not mod_valido:
                        nuevoModelo = input("Ingrese el nuevo modelo del vehiculo: ")

                        try:
                            VerificationExceptions.hayAlgo(nuevoModelo)
                            modificar_etiqueta(xml_path, "vehiculo", "descripcion/modelo",
                                               id, nuevoModelo)
                            mod_valido = True

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "5":
                    anio_valido = False

                    while not anio_valido:
                        nuevoAnio = int(input("Ingrese el nuevo anio de fabricacion del vehiculo: "))

                        try:
                            VerificationExceptions.hayAlgo(nuevoAnio)
                            VerificationExceptions.formatoFechaVehiculo(nuevoAnio)
                            modificar_etiqueta(xml_path, "vehiculo", "anioFabricacion",
                                               id, nuevoAnio)
                            anio_valido = True

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "6":
                    tar_valida = False

                    while not tar_valida:
                        nuevaTarifa = float(input("Ingrese la nueva tarifa por dia del vehiculo: "))
                        try:
                            VerificationExceptions.hayAlgo(nuevaTarifa)
                            VerificationExceptions.esNum(nuevaTarifa)
                            modificar_etiqueta(xml_path, "vehiculo", "tarifaDia", id,
                                               nuevaTarifa)
                            tar_valida = True

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "7":
                    est_valido = False

                    while not est_valido:
                        nuevoEstado = input(
                            "Ingrese el nuevo estado del vehículo (disponible, alquilado o mantenimiento): ")
                        try:
                            VerificationExceptions.disp_correcto(nuevoEstado)
                            modificar_etiqueta(xml_path, "vehiculo", "estado", id, nuevoEstado)
                            est_valido = True

                        except VerificationExceptions.MisExceptions as err:
                            print(err)

                    salir = True

                elif opc == "0":
                    salir = True
                    print('Saliendo...')

                else:
                    print("Opcion no valida")

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


def buscar_vehiculo(matricula, xml_path):
    """
    Funcion para buscar un vehiculo por matricula
    :param matricula: recibe la matricula del vehiculo
    :param xml_path: recibe el fichero en el que vamos a guardar los datos
    :return:
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for vehiculo in root.findall('vehiculo'):
            mat_vehi = vehiculo.find('matricula').text

            if mat_vehi == matricula:
                id_vehiculo = vehiculo.get('id')
                matricula = vehiculo.find('matricula').text
                marca = vehiculo.find('descripcion/marca').text
                modelo = vehiculo.find('descripcion/modelo').text
                anio_fabricacion = vehiculo.find('anioFabricacion').text
                tarifa_dia = vehiculo.find('tarifaDia').text
                estado = vehiculo.find('estado').text

                print(f'''****VEHICULO****
 Id: {id_vehiculo}
 Matricula: {matricula}
 Marca: {marca}
 Modelo: {modelo}
 Anio de Fabricacion: {anio_fabricacion}
 Tarifa Diaria: {tarifa_dia}
 Estado: {estado}        
 ***********************''')

    except FileNotFoundError:
        print("No hay vehiculos guardados")
    except Exception as e:
        print(f"Error: {e}")


# ******************** FUNCIONES  ALQUILER **************************************

def crearAlquiler(dni, fechaIni, fechaFin, kmIni, idVe):
    """
    Funcion crear un alquiler que lo guarda en el fichero de alquleres.xml
    :param dni: Recibe dni del cliente
    :param fechaIni: Recibe la fecha de inicio
    :param fechaFin: Recibe la fecha final
    :param kmIni: Recibe los kilometros iniciales
    :param idVe: Recibe la id de vehiculo
    :return:
    """
    try:
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
    except FileNotFoundError:
        root = Element('alquileres')
        tree = ET.ElementTree(root)

    # Creamos el alquiler y su atributo
    alquiler = ET.Element('alquiler')
    alquiler.set('id', str(obtId('alquileres.xml', "alquiler")))

    # Creamos sus atributos o subelementos
    ET.SubElement(alquiler, 'id_vehiculo').text = idVe
    ET.SubElement(alquiler, 'dni').text = dni
    ET.SubElement(alquiler, 'fecha_inicio').text = fechaIni
    ET.SubElement(alquiler, 'fecha_final').text = fechaFin
    ET.SubElement(alquiler, 'kilometros_inicio').text = str(kmIni)
    ET.SubElement(alquiler, 'fecha_devolucion').text = ''
    ET.SubElement(alquiler, 'kilometros_final').text = ''
    ET.SubElement(alquiler, 'precio_final').text = ''
    ET.SubElement(alquiler, 'recargo').text = ''
    ET.SubElement(alquiler, 'estado').text = 'Activo'

    # Agregamos el nuevo alquiler
    root.append(alquiler)

    # Guardamos el archivo XML actualizado
    salida = prettify(root)
    file = open("alquileres.xml", "w")
    file.write(salida)
    eliminarEspacios("alquileres.xml")
    file.close()
    eliminarEspacios('alquileres.xml')

    tree2 = ET.parse('vehiculos.xml')
    root2 = tree2.getroot()
    for elemento in root2.iter('vehiculo'):
        if (elemento.get('id') == idVe):
            elemento.find('estado').text = 'alquilado'
    tree2.write('vehiculos.xml')


def obtIdVe(matVe):
    """
    Funcion para obtener la id de un vehiculo en caso de no encontrarla devuelve un -1
    :param matVe: Recibe la matricula de un vehiculo
    :return: Retorna la id si la encuentra o -1 en caso contrario
    """
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        idVe = elemento.get('id')
        if (elemento.find('matricula').text == matVe):
            return idVe
    return -1


def finAlquiler(fechaDevo, kmFin, id):
    """
    Funcion para guardar los datos recibidos por parametros para finalizar un alquiler
    :param fechaDevo: Recibe la fecha de devolucion
    :param kmFin: Recibe los kilometros finales
    :param id: Recibe la id del alquiler
    :return:
    """
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        for elemento in root.iter('alquiler'):
            if (elemento.get('id') == id):
                fechaIni = elemento.find('fecha_inicio').text
                fechaFin = elemento.find('fecha_final').text
                idVe = elemento.find('id_vehiculo').text
                elemento.find('fecha_devolucion').text = fechaDevo
                elemento.find('kilometros_final').text = kmFin
                auxFin = datetime.strptime(fechaFin, '%Y-%m-%d')
                auxDev = datetime.strptime(fechaDevo, '%Y-%m-%d')
                preciFin = elemento.find('precio_final')
                recargo = elemento.find('recargo')
                diasR = (auxDev - auxFin).days
                if (diasR > 0):
                    recargo.text = str(diasR * 80)
                else:
                    recargo.text = 0
                preciFin.text = str(precioFin(fechaIni, fechaFin, idVe) + int(recargo.text))
                elemento.find('estado').text = 'Finalizado'

                tree.write('alquileres.xml')
                tree2 = ET.parse('vehiculos.xml')
                root2 = tree2.getroot()
                for elemento in root2.iter('vehiculo'):
                    if (elemento.get('id') == idVe):
                        elemento.find('estado').text = 'disponible'
                tree2.write('vehiculos.xml')


def mostrarTodoAlq():
    """
    Funcion que muestra los datos del los alquileres del fichero
    :return:
    """
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()

        if not root.findall('alquiler'):
            print("No hay alquileres guardados")
        else:
            print("========== LISTADO ALQUILERES ==========")
            for elemento in root.iter('alquiler'):
                idAlquiler = elemento.get('id')
                idVehiculo = elemento.find('id_vehiculo').text
                dni = elemento.find('dni').text
                fechaIni = elemento.find('fecha_inicio').text
                fechaFin = elemento.find('fecha_final').text
                kmIni = elemento.find('kilometros_inicio').text
                kmFin = elemento.find('kilometros_final').text
                precio = elemento.find('precio_final').text
                rec = elemento.find('recargo').text
                est = elemento.find('estado').text

                print(f'''****Alquiler****
Id: {idAlquiler}
Id Vehiculo: {idVehiculo}
DNI Cliente: {dni}
Fecha Inicio: {fechaIni}
Fecha Finalizacion: {fechaFin}
Kilometros Inicio: {kmIni}
Kilometros Finalizacion: {kmFin}
Precio Final: {precio}        
Recargo: {rec}
Estado: {est}
***********************''')
    else:
        print("No hay alquileres aun")


def precioFin(fechaIni, fechaFin, idVe):
    """
    Funcion para calcular el precio final
    :param fechaIni: recibe la fecha incial
    :param fechaFin: Recibe la fecha final
    :param idVe: Recibe la id del Vehiculo
    :return: Retorna la el precio final y calculado
    """
    tarifa = 0
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    for elemento in root.iter('vehiculo'):
        if (elemento.get('id') == idVe):
            tarifa = float(elemento.find('tarifaDia').text)
    fecha1 = datetime.strptime(fechaIni, '%Y-%m-%d')
    fecha2 = datetime.strptime(fechaFin, '%Y-%m-%d')
    dias = int((fecha2 - fecha1).days)
    return tarifa * dias


def listado_coches_disponibles():
    """
        Funcion para obtener un listado de vehiculos disponibles del dni recibido
        :return: Retorna un diccionario con los vehiculos disponibles
        """
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()
    dicVeh = {}
    for elemento in root.iter('vehiculo'):
        idVe = elemento.get('id')
        matVe = elemento.find('matricula').text
        marca = elemento.find('descripcion/marca').text
        modelo = elemento.find('descripcion/modelo').text
        estado = elemento.find('estado').text
        if (estado == 'disponible'):
            dicVeh[idVe] = {'mat': matVe, 'marca': marca, 'modelo': modelo}

    return dicVeh


def diponibles():
    """
    Funcion que comprueba si hay vehiculos disponibles
    :return: Retorna True si encuentra alguno disponibles y False en caso contrario
    """
    tree = ET.parse('vehiculos.xml')
    root = tree.getroot()

    for elemento in root.iter('vehiculo'):
        estado = elemento.find('estado').text
        if (estado == 'disponible'):
            return True

    return False


def alquiDisp(dniRec):
    """
    Funcion para obtener un listado de alquileres activo del dni recibido
    :param dniRec: Recibe el dni para buscarlo
    :return: Retorna un diccionario de alqulieres activos
    """
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        dicAlq = {}
        for elemento in root.iter('alquiler'):
            idAlq = elemento.get('id')
            idVeh = elemento.find('id_vehiculo').text
            dni = elemento.find('dni').text
            fechaIni = elemento.find('fecha_inicio').text
            if (dni == dniRec and elemento.find('estado').text == 'Activo'):
                dicAlq[idAlq] = {'Id_Vehiculo': idVeh, 'dni': dni, 'Fecha_Inicio': fechaIni}
        return dicAlq


def alquileres_activos():
    """
    Funcion que comprueba si hay alquileres Activos
    :return: Retorna True si encuentra alguno activo y False en caso contrario
    """
    if (Path('alquileres.xml').exists()):
        tree = ET.parse('alquileres.xml')
        root = tree.getroot()
        for elemento in root.iter('alquiler'):
            if (elemento.find('estado').text == 'Activo'):
                return True
        return False


def mostrar_por_elemento(etiqueta, abuscar):
    """
    Funcion que muestra un alquiler dependiendo de los paramatros que recibe
    :param etiqueta: Recibe la etiqueta del elemento a buscar
    :param abuscar: Recibe el texto a buscar
    :return:
    """
    tree = ET.parse('alquileres.xml')
    root = tree.getroot()
    existencias = False
    for elemento in root.iter('alquiler'):
        idAlquiler = elemento.get('id')
        idVehiculo = elemento.find('id_vehiculo').text
        dni = elemento.find('dni').text
        fechaIni = elemento.find('fecha_inicio').text
        fechaFin = elemento.find('fecha_final').text
        kmIni = elemento.find('kilometros_inicio').text
        kmFin = elemento.find('kilometros_final').text
        precio = elemento.find('precio_final').text
        rec = elemento.find('recargo').text
        est = elemento.find('estado').text
        aux = elemento.find(etiqueta).text
        if (aux == abuscar):
            existencias = True
            print(f'''****Alquiler****
Id: {idAlquiler}
Id Vehiculo: {idVehiculo}
DNI Cliente: {dni}
Fecha Inicio: {fechaIni}
Fecha Finalizacion: {fechaFin}
Kilometros Inicio: {kmIni}
Kilometros Finalizacion: {kmFin}
Precio Final: {precio}        
Recargo: {rec}
Estado: {est}
***********************''')
    if (existencias is False):
        print(f"No hay alquileres con {etiqueta} = {abuscar}")


def mostrar_por_atributo(abuscar):
    """
    Funcion que muestra un alquiler dependiendo de los paramatros que recibe
    :param abuscar: Recibe el texto a buscar
    :return:
    """
    tree = ET.parse('alquileres.xml')
    root = tree.getroot()
    for elemento in root.iter('alquiler'):
        idAlquiler = elemento.get('id')
        idVehiculo = elemento.find('id_vehiculo').text
        dni = elemento.find('dni').text
        fechaIni = elemento.find('fecha_inicio').text
        fechaFin = elemento.find('fecha_final').text
        kmIni = elemento.find('kilometros_inicio').text
        kmFin = elemento.find('kilometros_final').text
        precio = elemento.find('precio_final').text
        rec = elemento.find('recargo').text
        est = elemento.find('estado').text
        aux = elemento.get('id')
        if (aux == abuscar):
            print(f'''****Alquiler****
            Id: {idAlquiler}
            Id Vehiculo: {idVehiculo}
            DNI Cliente: {dni}
            Fecha Inicio: {fechaIni}
            Fecha Finalizacion: {fechaFin}
            Kilometros Inicio: {kmIni}
            Kilometros Finalizacion: {kmFin}
            Precio Final: {precio}        
            Recargo: {rec}
            Estado: {est}
            ***********************''')


# ******************** FUNCIONES  COMUNES **************************************

def obtId(fichero, etiqueta):
    """
    Funcion para generar ids automaitcas que no sean repetidas
    :param fichero: Recibe el fichero
    :param etiqueta: Recibe la etiqueta para iterar
    :return:
    """
    aux = 1
    if (Path(fichero).exists()):
        tree = ET.parse(fichero)
        root = tree.getroot()
        for elemento in root.iter(etiqueta):
            id = int(elemento.get("id"))
            if (id >= aux):
                aux = id
    else:
        return aux
    return aux + 1


def eliminarEspacios(fichero):
    """
    Funcion para eliminar las lineas vacias que se van creando con la funcion prettify
    :param fichero: Recibe el fichero
    :return:
    """
    if (Path(fichero).exists()):
        with open(fichero, 'r') as file:
            contenido = file.read()
        lineas = [linea for linea in contenido.splitlines() if linea.strip()]
        contenidioSin = '\n'.join(lineas)
        with open(fichero, 'w') as file:
            file.write(contenidioSin)


def prettify(elem):
    """
    Funcion para formatear el documento
    :param elem: Recibe el elemento a formatear
    :return:
    """
    from xml.etree import ElementTree
    from xml.dom import minidom

    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def modificar_etiqueta(fichero, iterable, etiqueta, id_elemento, texto_cambio):
    """
    Funcion para modificar el texto de un elemento
    :param fichero: Recibe el nombre del fichero
    :param iterable: Recibe el elemento a iterar
    :param etiqueta: Recibe la etiqueta del elemento que queremos cambiar el texto
    :param id_elemento: Recibe la id del que queremos modificar
    :param texto_cambio: Recibe el texto a introducir en el elemento
    :return:
    """
    salir = False
    tree = ET.parse(fichero)
    root = tree.getroot()
    elem = None

    for elemento in root.iter(iterable):
        id = elemento.get('id')
        elem = elemento.find(etiqueta)
        if id == id_elemento:
            elemento.find(etiqueta).text = texto_cambio

    while not salir:
        op = input("Quieres guardar los cambios generados?[S/N]").lower()
        if op == "s":
            tree.write(fichero)
            if (fichero == 'alquileres.xml' and etiqueta == 'id_vehiculo'):
                tree2 = ET.parse('vehiculos.xml')
                root2 = tree2.getroot()
                for element in root2.iter():
                    if (element.get('id') == texto_cambio):
                        element.find('estado').text = 'alquilado'
                    if (element.get('id') == elem):
                        element.find('estado').text = 'disponible'
                tree2.write('vehiculos.xml')
            salir = True
            print("Cambios guardados.")
        elif op == "n":
            salir = True;
            print("Saliendo sin guardar...")
        else:
            print("Entrada no valida.")


def existe_id(fichero, id, etiquieta):
    """
    Funcion que comprueba si existe una id
    :param fichero: Recibe el nombre del fichero
    :param id: Recibe el id
    :param etiquieta: Recibe la etiqueta a iterar
    :return: Retorna True si existe False en caso de que no
    """
    tree = ET.parse(fichero)
    root = tree.getroot()
    for elemento in root.iter(etiquieta):
        id_aux = elemento.get('id')
        if (id == id_aux):
            return True
    return False


def modificar_atributo(fichero, iterable, id_elemento, textoCambio):
    """
    Funcion para modificar un atributo que en este caso serian las ids
    :param fichero: Recibe el nombre del fichero
    :param iterable: Recibe el elemento a iterar
    :param id_elemento: Recibe el id
    :param textoCambio: Recibe el texto del elemento que queremos cambiar que en este caso son las ids
    :return:
    """
    salir = False
    tree = ET.parse(fichero)
    root = tree.getroot()

    for elemento in root.iter(iterable):
        id = elemento.get('id')
        if (id == id_elemento):
            elemento.set("id", textoCambio)

    while not salir:
        op = input("Quieres guardar los cambios generados?[S/N]").lower()

        if op == "s":
            tree.write(fichero)
            salir = True
            print("Cambios guardados, saliendo...")
        elif op == "n":
            salir = True;
            print("Saliendo sin guardar...")
        else:
            print("Entrada no valida.")


def obt_elemento(fichero, id, iterador, etiqueta):
    """
    Funcion para obtener el texto de un elemento del fichero
    :param fichero: Recibe el fichero donde debe buscar
    :param id: Recibe la id del elemento que queremos
    :param iterador: Recibe la etiqueta que vamos a iterar
    :param etiqueta: Recibe la etiqueta del elemento que queremos
    :return: Retorna el texto del elemento si lo encuentra en caso contrario retorna None
    """
    tree = ET.parse(fichero)
    root = tree.getroot()
    for elemento in root.iter(iterador):
        if (elemento.get('id') == id):
            return elemento.find(etiqueta).text
    return None
