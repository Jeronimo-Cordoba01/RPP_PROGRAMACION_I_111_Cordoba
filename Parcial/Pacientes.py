import csv, json, random, datetime, os
from Inputs import *
from os import system

class Pacientes:
    """
    La clase Pacientes es una representación de un paciente individual y contiene varios atributos que describen su información personal y médica.
    Constructor (__init__):
    •	Parámetros:
        o	iden (int): Identificador único del paciente.
        o	nombre (str): Nombre del paciente.
        o	apellido (str): Apellido del paciente.
        o	edad (int): Edad del paciente.
        o	altura (int): Altura del paciente en centímetros.
        o	peso (float): Peso del paciente en kilogramos.
        o	dni (int): Número de documento nacional de identidad (DNI) del paciente.
        o	grupo_sanguineo (str): Grupo sanguíneo del paciente.
    •	Acciones:
        o	Inicializa los atributos del objeto Pacientes con los valores proporcionados.
    Método __str__:
    •	Descripción:
        o	Devuelve una representación en cadena del objeto Pacientes, que incluye todos sus atributos.
    •	Retorno:
        o	Una cadena que contiene el identificador, nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo del paciente.

    """
    def __init__(self, iden: int, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str):
        self.iden = iden
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dni = dni
        self.grupo_sanguineo = grupo_sanguineo
        
    def __str__(self):
        return f"{self.iden} {self.nombre} {self.apellido} {self.edad} {self.altura} {self.peso} {self.dni} {self.grupo_sanguineo}"
    
class Enfermero:
    """
    La clase Enfermero contiene métodos para administrar pacientes, como ingresar nuevos pacientes, buscar pacientes por DNI, 
    modificar información de pacientes, eliminar pacientes, mostrar información de pacientes 
    y realizar otras operaciones relacionadas con pacientes.
    Constructor (__init__):
    •	Acciones:
        o	Inicializa la lista de pacientes vacía.
        o	Lee el archivo CSV de pacientes (Pacientes.csv) al instanciar un objeto de la clase Enfermero.
    Método ingreso_pacientes:
    •	Descripción:
        o	Permite al usuario ingresar información para un nuevo paciente.
        o	Valida la entrada de datos utilizando funciones de validación proporcionadas por el módulo Inputs.py.
        o	Agrega el nuevo paciente a la lista de pacientes si la entrada es válida.
    •	Acciones:
        o	Solicita al usuario ingresar información para un nuevo paciente, incluyendo identificador, nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo.
        o	Utiliza funciones de validación del módulo Inputs.py para validar la entrada de datos.
        o	Crea un nuevo objeto Pacientes con la información ingresada.
        o	Agrega el nuevo paciente a la lista de pacientes.
        o	Imprime un mensaje indicando si el paciente fue ingresado correctamente.
        o	Llama al método escribir_JSON() para escribir la lista actualizada de pacientes en un archivo JSON.
    Otros Métodos:
    •	buscar_DNI: Busca un paciente por su DNI en la lista de pacientes.
    •	Otros métodos no incluidos en la sección de código proporcionada podrían incluir operaciones como modificar pacientes, eliminar pacientes, mostrar todos los pacientes y realizar otras operaciones relacionadas con pacientes.

    """
    def __init__(self, lista_pacientes: list[dict]):
        self.lista_pacientes = lista_pacientes 
        self.leer_CSV("Pacientes.csv")

    def ingreso_pacientes(self):
        """
        Ingresa un nuevo paciente. Valida que los datos sean correctos llamando desde "Inputs.py" a las funciones correspondientes. 
        Luego, agrega el paciente a la lista de Pacientes. Si el paciente ya existe, imprime un mensaje de error. 
        """
        
        iden = self.generar_identificador()
        
        iden = iden_valida("Ingrese el identificador del paciente: ")
        if not iden:
            print("Identificador inválido. Operación cancelada.")
            return
        
        nombre = nombre_apellido_valida("Ingrese el nombre del paciente: ", 3, 20).capitalize()
        if not nombre:
            print("Nombre inválido. Operación cancelada.")
            return

        apellido = nombre_apellido_valida("Ingrese el apellido del paciente: ", 3, 20).capitalize()
        if not apellido:
            print("Apellido inválido. Operación cancelada.")
            return

        edad = edad_valida("Ingrese la edad del paciente: ")
        if not edad:
            print("Edad inválida. Operación cancelada.")
            return

        altura = altura_valida("Ingrese la altura del paciente: ")
        if not altura:
            print("Altura inválida. Operación cancelada.")
            return

        peso = peso_valida("Ingrese el peso del paciente: ")
        if not peso:
            print("Peso inválido. Operación cancelada.")
            return

        dni = dni_valida("Ingrese el dni del paciente: ")
        if not dni:
            print("DNI inválido. Operación cancelada.")
            return

        grupo_sanguineo = grupo_sanguineo_valida("Ingrese el grupo sanguíneo del paciente: ")
        if not grupo_sanguineo:
            print("Grupo sanguíneo inválido. Operación cancelada.")
            return

        paciente = Pacientes(iden, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        self.lista_pacientes.append(paciente)
        self.escribir_CSV("Pacientes.csv")

        print("Paciente ingresado correctamente.")
        
    def generar_identificador(self) -> int:
        """
        •	Descripción:
            o	Este método se encarga de generar un identificador único para un nuevo paciente.
            o	Recorre la lista de pacientes para encontrar el identificador más alto actualmente en uso.
            o	Incrementa este identificador en uno para generar un nuevo identificador único.
        •	Parámetros:
            o	No recibe parámetros explícitos, pero accede a la lista de pacientes almacenada en el objeto Enfermero.
        •	Valor de Retorno:
            o	Retorna un entero que representa el identificador generado para un nuevo paciente.
        """
        id_autoincremental = 0
        for paciente in self.lista_pacientes:
            if paciente.iden > id_autoincremental:
                id_autoincremental = paciente.iden
        return id_autoincremental + 1

    def buscar_DNI(self, dni):
        """
        •	Descripción:
            o	Este método busca un paciente en la lista de pacientes por su número de documento nacional de identidad (DNI).
            o	Recorre la lista de pacientes y compara el DNI de cada paciente con el DNI proporcionado como argumento.
        •	Parámetros:
            o	dni (int): El número de DNI que se utilizará para buscar al paciente.
        •	Valor de Retorno:
            o	Retorna el objeto Pacientes correspondiente al paciente encontrado si se encuentra un paciente con el DNI proporcionado.
            o	Retorna None si no se encuentra ningún paciente con el DNI especificado.

        """
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                return paciente
        return None
        
#1. Dar de alta. Pedira los datos necesarios y dará de alta a un nuevo paciente, asignando un ID autoincremental.
    def dar_alta(self) -> bool:
        """
        Propósito
            El método dar_alta es responsable de agregar un nuevo paciente a la lista de pacientes después de verificar 
            que el paciente no está ya registrado mediante su DNI.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        Retorno:
            bool: Retorna True si el paciente se registra exitosamente, False en caso contrario (ya registrado o se cancela el alta).
        """
        id_autoincremental = self.generar_identificador()
        
        dni = dni_valida("Ingrese el DNI del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("El paciente ya está registrado.")
                return False
        
        alta()
        
        opcion = input("Opción: ").strip()
        if opcion == "1":
            self.ingreso_pacientes(id_autoincremental)
            self.escribir_JSON()
            return True
        elif opcion == "2":
            print("No se realizó el alta del paciente.")
            return False
        else:
            print("Opción inválida.")
            return False
#2. Modificar. Permitira alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar
    def modificar_paciente(self):
        """
        Propósito:
            Permite modificar los datos de un paciente existente en la lista de pacientes, identificado mediante su DNI.
        
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        
        Valor de Retorno:
            No retorna un valor explícito, pero imprime mensajes para informar al usuario sobre el resultado de la operación.
        """
        dni = dni_valida("Ingrese el DNI del paciente a modificar: ")
        paciente = self.buscar_DNI(dni)
        
        if paciente:
            print("Datos actuales del paciente:")
            print(paciente)
                
            opcion = input("Opción:  1. Modificar.  2. Cancelar.").strip()
            if opcion == "1":
                print("Ingrese los nuevos datos del paciente:")
                nombre = nombre_apellido_valida("Ingrese el nombre del paciente: ", 3, 20).capitalize()
                apellido = nombre_apellido_valida("Ingrese el apellido del paciente: ", 3, 20).capitalize()
                edad = edad_valida("Ingrese la edad del paciente: ")
                altura = altura_valida("Ingrese la altura del paciente: ")
                peso = peso_valida("Ingrese el peso del paciente: ")
                grupo_sanguineo = grupo_sanguineo_valida("Ingrese el grupo sanguíneo del paciente: ")
                
                paciente.nombre = nombre
                paciente.apellido = apellido
                paciente.edad = edad
                paciente.altura = altura
                paciente.peso = peso
                paciente.grupo_sanguineo = grupo_sanguineo
                
                print("Paciente modificado correctamente.")
            elif opcion == "2":
                print("Modificación cancelada.")
        else:
            print("No se encontró ningún paciente con el DNI proporcionado.")
#3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedira el DNI del paciente a eliminar.            
    def eliminar_paciente(self):
        """
        Propósito:
            Eliminar un paciente de la lista de pacientes, identificado mediante su DNI, después de obtener la confirmación del usuario.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        Retorno:
            No retorna un valor explícito, pero imprime mensajes para informar al usuario sobre el resultado de la operación.
        """
        dni = dni_valida("Ingrese el DNI del paciente a eliminar: ")
        paciente = self.buscar_DNI(dni)
        
        if paciente:
            opcion = input("Opción:  1. Eliminar.  2. Cancelar.").strip()
            if opcion == "1":
                self.lista_pacientes.remove(paciente)
                print("Paciente eliminado correctamente.")
                self.eliminar_JSON(paciente.dni)
            elif opcion == "2":
                print("Eliminación cancelada.")
        else:
            print("Paciente no encontrado.")
        
#4. Mostrar todos los pacientes.                
    def mostrar_todosLos_pacientes(self):
        """
        Propósito:
            Mostrar una lista de todos los pacientes almacenados en el archivo Pacientes.csv.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene métodos auxiliares y posiblemente atributos de la clase.
        Valor de Retorno:
            No retorna un valor explícito, pero imprime la lista de pacientes al usuario.
        """
        if not self.lista_pacientes:
            print("No hay pacientes para mostrar.")
            return
        
        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("-----------------------------------------------------------------------------------------")
        for paciente in self.lista_pacientes:
            print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
        print("*****************************************************************************************")
        
#5. Ordenar pacientes. Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por: 
    def Ordenar(self):
        """
        Función:
            Proporcionar una funcionalidad para ordenar la lista de pacientes según diversos criterios 
            (nombre, apellido, altura, grupo sanguíneo) en orden ascendente o descendente, basada en la entrada del usuario.
        Argumentos
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        Valor de Retorno
            No retorna un valor explícito, pero imprime mensajes informativos sobre el estado del ordenamiento al usuario.
        """ 
        def bubble_sort(arr, key, ascendente=True):
            num_pacientes = len(arr)
            for pase in range(num_pacientes):
                for posicion in range(0, num_pacientes - pase - 1):
                    if ascendente:
                        if arr[posicion].__dict__[key] > arr[posicion + 1].__dict__[key]:
                            arr[posicion], arr[posicion + 1] = arr[posicion + 1], arr[posicion]
                    else:
                        if arr[posicion].__dict__[key] < arr[posicion + 1].__dict__[key]:
                            arr[posicion], arr[posicion + 1] = arr[posicion + 1], arr[posicion]

        def ordenar_por(tipo: str, ascendente: bool = True):
            try:
                match tipo:
                    case "nombre":
                        bubble_sort(self.lista_pacientes, "nombre", ascendente)
                    case "apellido":
                        bubble_sort(self.lista_pacientes, "apellido", ascendente)
                    case "altura":
                        bubble_sort(self.lista_pacientes, "altura", ascendente)
                    case "grupo_sanguineo":
                        bubble_sort(self.lista_pacientes, "grupo_sanguineo", ascendente)
                    case "salir":
                        return
                    case _:
                        print("Tipo de ordenamiento inválido.")
                        return
                print(f"Pacientes ordenados por {tipo} de forma {'ascendente' if ascendente else 'descendente'}.")
            except AttributeError as e:
                print(f"Error en la ordenación: {e}")

        menu_ordenar()
        opcion = input("Selecciona una opción de ordenamiento: ").strip()
        ascendente = input("Orden ascendente (s/n): ").strip().lower() == 's'
        
        match opcion:
            case "1":
                ordenar_por("nombre", ascendente)
            case "2":
                ordenar_por("apellido", ascendente)
            case "3":
                ordenar_por("altura", ascendente)
            case "4":
                ordenar_por("grupo_sanguineo", ascendente)
            case _:
                print("Opción inválida.")
    
#6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
    def mostrar_paciente_por_DNI(self):
        """
        Descripción:
            Permite al usuario buscar y mostrar información detallada de un paciente específico en la lista de pacientes 
            usando su DNI (Documento Nacional de Identidad).
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        Retorno:
            No retorna un valor explícito, pero imprime información del paciente encontrado o un mensaje de error si no se encuentra.
        """
        dni = dni_valida("Ingrese el DNI del paciente a buscar: ")
        paciente = self.buscar_DNI(dni)
        
        if paciente:
            print("Paciente encontrado:")
            print(paciente)
        else:
            print("Paciente no encontrado.")
    
#7 calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio de:
    def promedio(self):
        """
        Propósito:
            Calcular y mostrar los promedios de edad, altura y peso de los pacientes registrados en la lista de pacientes.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes.
        Valor de Retorno:
            No retorna un valor explícito, pero imprime los promedios calculados de edad, altura y peso de los pacientes.
        """
        if not self.lista_pacientes:
            print("No hay pacientes registrados.")
            return

        tipo = input("Ingrese el tipo de promedio a calcular (edad, altura, peso): ").strip().lower()
        
        suma = 0
        total = len(self.lista_pacientes)
        
        for paciente in self.lista_pacientes:
            match tipo:
                case "edad":
                    suma += paciente.edad
                case "altura":
                    suma += paciente.altura
                case "peso":
                    suma += paciente.peso
                case _:
                    print("Tipo de promedio no válido.")
                    return
        
        promedio = suma / total
        if tipo == "edad":
            print(f"Promedio de edad de los pacientes: {promedio}")
        elif tipo == "altura":
            print(f"Promedio de altura de los pacientes: {promedio} cm")
        elif tipo == "peso":
            print(f"Promedio de peso de los pacientes: {promedio} kg")
        
#8. Mostrar todos los pacientes: Mostrar una lista de todos los pacientes almacenados en el archivo Pacientes.csv.
    def determinar_compatibilidad(self):
        """
        Descripción:
            Determina la compatibilidad entre dos grupos sangineos.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes y métodos auxiliares.
        Retorno:
            No retorna un valor explícito, pero imprime la compatibilidad entre los dos grupos sangineos.
        """
        dni = dni_valida("Ingrese el DNI del paciente: ")
        paciente = self.buscar_DNI(dni)
        
        if paciente:
            compatibilidad = {
                "A+": {"Donar": ["A+", "AB+"], "Recibir": ["O+", "O-", "A+", "A-"]},
                "A-": {"Donar": ["A-", "AB-"], "Recibir": ["O-", "O+", "A-", "A+"]},
                "B+": {"Donar": ["B+", "AB+"], "Recibir": ["O+", "O-", "B+", "B-"]},
                "B-": {"Donar": ["B-", "AB-"], "Recibir": ["O-", "O+", "B-", "B+"]},
                "AB+": {"Donar": ["AB+", "O+"], "Recibir": ["O+", "O-", "AB+", "AB-"]},
                "AB-": {"Donar": ["AB-", "O-"], "Recibir": ["O-", "O+", "AB-", "AB+"]},
                "O+": {"Donar": ["O+", "AB+"], "Recibir": ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]},
                "O-": {"Donar": ["O-", "AB-"], "Recibir": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]},                
            }
            
        grupo_compatible = paciente.grupo_sanguineo
        
        if grupo_compatible in compatibilidad:
            puede_donar = compatibilidad[grupo_compatible]["Donar"]
            puede_recibir = compatibilidad[grupo_compatible]["Recibir"]
            
            print(f"El paciente {paciente} puede donar a: {', '.join(puede_donar)}")
            print(f"El paciente {paciente} puede recibir de: {', '.join(puede_recibir)}")
            
            posibles_donantes = []
            for donante in self.lista_pacientes:
                if donante.grupo_sanguineo in puede_donar:
                    posibles_donantes.append(donante)
            
            if posibles_donantes:
                    print("Posibles donantes:")
                    for donante in posibles_donantes[:3]:
                        print(donante)
                    else:
                        print("No hay donantes compatibles.")
            else:
                print("Grupo sanguíneo no reconocido.")
        else:
            print("Paciente no encontrado.")
#9. Salir. Terminará la ejecución del programa.
    def salir(self):
        """
        •	Descripción:
            o	Este método terminará la ejecución del programa.
            o	Simplemente muestra un mensaje de despedida y finaliza la ejecución del programa.
        •	Valor de Retorno:
            o	None: No hay valor de retorno explícito, ya que este método simplemente termina la ejecución del programa.

        """
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        return
        
#0. Mostrar Matriz
    def crear_matriz():
        return [
            ["A+", 10, 4],
            ["A-", 5, 3],
            ["B+", 3, 9],
            ["B-", 2, 8],
            ["AB+", 8, 2],
            ["AB-", 7, 3],
            ["O+", 4, 10],
            ["O-", 1, 5],
        ]
        
    def mostrar_matriz(self):
        self.matriz = self.crear_matriz()
        print(f"{'Tipo':<3} {'Donar':<5} {'Recibir':<7}")
        for fila in self.matriz:
            tipo, donar, recibir = fila
            print(f"{tipo:<3} {donar:<5} {recibir:<7}")
#Aca lee el CSV
    def leer_CSV(self, path: str = "Pacientes.csv") -> list:
        """
        Propósito: 
        Leer datos de un archivo CSV que contiene información de pacientes y cargarlos en una lista de diccionarios.

        Argumentos:
        path: Ruta del archivo CSV a leer. Por defecto, se espera "Pacientes.csv" en el directorio actual.
        
        Valor de retorno: 
        Lista de diccionarios, cada uno representando un paciente con sus atributos.
        """
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        try:
            with open(ruta_absoluta, "r", encoding="utf8") as archivo:
                lector = csv.DictReader(archivo)
                for campos in lector:
                    paciente = Pacientes(
                        iden=int(campos["Iden"]),
                        nombre=campos["Nombre"],
                        apellido=campos["Apellido"],
                        edad=int(campos["Edad"]),
                        altura=int(campos["Altura"]),
                        peso=float(campos["Peso"]),
                        dni=int(campos["DNI"]),
                        grupo_sanguineo=campos["Sangre"]
                    )
                    self.lista_pacientes.append(paciente)
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_absoluta}")
        except csv.Error as e:
            print(f"Error al leer el archivo CSV: {e}")

#Guarda la lista de objetos en el CSV
    def guardar_CSV(self, pacientes: list, archivo: str):
        """
        Propósito:
            Guardar los datos de la lista de pacientes en un archivo CSV.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes.
            pacientes: Una lista de diccionarios, donde cada diccionario representa un paciente con sus atributos.
            archivo: Una cadena que especifica el nombre del archivo CSV en el cual se guardarán los datos.
        Valor de Retorno:
            No retorna un valor explícito, pero imprime un mensaje indicando el éxito o fracaso de la operación.
        """
        try:
            with open(archivo, 'w', newline='') as file:
                writer = csv.DictWriter(file, nombre_archivo=pacientes[0].keys())
                writer.writeheader()
                writer.writerows(pacientes)
            print("Datos guardados correctamente en el archivo CSV.")
        except IOError:
            print(f"No se pudo guardar el archivo {archivo}.")
                    
#Escribe la lista de objetos en el CSV
    def escribir_CSV(self, archivo: str):
        """
        Propósito:
            Escribir los datos de la lista de pacientes en un archivo CSV especificado.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes.
            archivo: Una cadena que especifica el nombre del archivo CSV en el cual se guardarán los datos.
        Valor de Retorno:
            No retorna un valor explícito, pero imprime un mensaje indicando el éxito o fracaso de la operación.
        """
        try:
            with open(archivo, 'w', newline='') as file:
                nombres = ["iden", "nombre", "apellido", "edad", "altura", "peso", "dni", "grupo_sanguineo"]
                writer = csv.DictWriter(file, nombres=nombres)
                writer.writeheader()
                for paciente in self.lista_pacientes:
                    writer.writerow({
                        "iden": paciente.iden,
                        "nombre": paciente.nombre,
                        "apellido": paciente.apellido,
                        "edad": paciente.edad,
                        "altura": paciente.altura,
                        "peso": paciente.peso,
                        "dni": paciente.dni,
                        "grupo_sanguineo": paciente.grupo_sanguineo
                    })
            print("Datos guardados correctamente en el archivo CSV.")
        except IOError:
            print(f"No se pudo guardar el archivo {archivo}.")

#Dar de alta en JSON
    def escribir_JSON(self):
        """
        Propósito:
            Guardar los datos de la lista de pacientes en un archivo JSON especificado.
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes.
            archivo: Una cadena que especifica el nombre del archivo JSON en el cual se guardarán los datos.
        Valor de Retorno:
            No retorna un valor explícito, pero imprime un mensaje indicando el éxito o fracaso de la operación.
        """
        try:
            with open("Alta.json", "w", encoding="utf-8", newline='') as file:
                lista_pacientes_dict = []
                
                for paciente in self.lista_pacientes:
                    paciente_dict = {
                        "iden": paciente.iden,
                        "nombre": paciente.nombre,
                        "apellido": paciente.apellido,
                        "edad": paciente.edad,
                        "altura": paciente.altura,
                        "peso": paciente.peso,
                        "dni": paciente.dni,
                        "grupo_sanguineo": paciente.grupo_sanguineo
                    }
                    lista_pacientes_dict.append(paciente_dict)
                
                json.dump(lista_pacientes_dict, file, indent=4)
            
            print("Datos guardados correctamente en el archivo JSON.")
        
        except IOError:
            print("No se pudo guardar el archivo Alta.json.")
            
#Eliminar en JSON
    def eliminar_JSON(self, id_paciente: int):
        """
        Propósito:
            Este método tiene como objetivo eliminar un paciente de la lista de pacientes y agregarlo a un archivo JSON 
            llamado "Muertos.json".
        Argumentos:
            self: Referencia a la instancia de la clase que contiene la lista de pacientes.
            id_paciente: El identificador único del paciente que se eliminará.
        Valor de Retorno:
            No retorna un valor explícito, pero maneja la eliminación del paciente de la lista de pacientes y 
            su adición al archivo JSON de pacientes eliminados.
        """
        try:
            with open("Muertos.json", "r") as f:
                pacientes_eliminados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pacientes_eliminados = []

        for paciente in self.lista_pacientes:
            if paciente.iden == id_paciente:
                pacientes_eliminados.append(paciente.__dict__)
                self.lista_pacientes.remove(paciente)
                break

        with open("Muertos.json", "w") as f:
            json.dump(pacientes_eliminados, f, indent=4)

            