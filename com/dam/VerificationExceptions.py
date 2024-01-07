from datetime import datetime


class MisExceptions(Exception):
    """
    Clase creada para generar nuestras propias excepciones
    """

    def __init__(self, message="Error"):
        self.message = message

        super().__init__(self.message)


def hayAlgo(cadena):
    """
        Funcion para comprobar si la cadena contiene algo en caso contrario lanza una excepcion
        :param cadena: recibe una cadena por el usuario
        :return:
        """
    if (len(cadena) == 0):
        raise MisExceptions('No se ha escrito nada')


def dniFormat(dni):
    """
    Funcion para comprobar si esta bien el formato del dni en caso contrario lanza una excepcion
    :param dni: recibe el dni escrito por el usuario
    :return:
    """
    if len(dni) != 9:
        raise MisExceptions('Debe tener 9 caractres')
    if not dni[:-1].isdigit():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')
    if not dni[-1].isalpha():
        raise MisExceptions('No se cumple con el formato. Debe tener 8 digitos y una letra.')


def matFormat(matricula):
    """
    Funcion para comprobar si la matricula del coche tiene bien el formato en caso contrario lanza una excepcion
    :param matricula: recibe la matricula escrita por el usuario
    :return:
    """
    if len(matricula) != 7:
        raise MisExceptions('Debe tener 7 caractres')
    if not matricula[:4].isdigit() or not matricula[4:].isalpha():
        raise MisExceptions(
            'La matrícula no cumple con el formato. Debe tener 4 dígitos y 3 letras.')


def esNum(num):
    """
    Funcion para comprobar si lo que escribe el usuario es un numero y si es positivo o en caso contrario lanza una excepcion
    :param num: recibe el numero escrito por el usuario
    :return:
    """
    try:
        if(int(num) < 0):
            raise MisExceptions("El numero no puede ser menor que 0")
    except Exception:
        raise MisExceptions('Debe introducir solo numeros')


def formatoFecha(fecha):
    """
    Funcion para comporbar que el formato de la fecha sea correcto en caso de que no lanza una excepcion
    :param fecha: recibe la fecha escrita por el usuario
    :return:
    """
    formato = "%Y-%M-%D"
    try:
        datetime.strptime(fecha, formato)

    except ValueError:
        raise MisExceptions('Formato de la fecha incorrecto. Formato esperado yyyy')


def formatoFechaVehiculo(fecha):
    """
    Funcion para comporbar que el formato de la fecha sea correcto en caso de que no lanza una excepcion
    :param fecha: recibe la fecha escrita por el usuario
    :return:
    """
    formato = "%Y"
    try:
        datetime.strptime(fecha, formato)

    except ValueError:
        raise MisExceptions('Formato de la fecha incorrecto. Formato esperado yyyy')


def disp_correcto(disp):
    """
    Funcion para comprobar que se introduce bien el estado de un vehiculo y que sea una de las tres que
    queremos.
    :param disp: recibe disp que es el input del estado dado por el susuario
    :return:
    """
    if (disp.lower() != 'disponible' and disp.lower() != 'alquilado' and disp.lower() != 'mantenimiento'):
        raise MisExceptions('La disponibilidad debe ser una de las tres: disponible, alquilado o mantenimiento')


def dife_fechas(fecha_menor, fecha_mayor):
    """
    Funcion para comprobar que no se introduzcan fechas que puedan ser anteriores a la fecha de alquiler incial en caso contrario
    se lanzara una excepcion
    :param fecha_menor: Recibe la fecha de inicio
    :param fecha_mayor: recibe la fecha final
    :return:
    """
    fecha_menor = datetime.strptime(fecha_menor, "%Y-%m-%d")
    fecha_mayor = datetime.strptime(fecha_mayor, "%Y-%m-%d")
    num = int((fecha_mayor - fecha_menor).days)
    if (num <= 0):
        raise MisExceptions('No se puede hacer alquileres menores a un dia')
