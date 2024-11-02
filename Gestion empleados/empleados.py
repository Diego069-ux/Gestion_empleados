import mysql.connector
import smtplib
from email.mime.text import MIMEText
import os

#Apartado empleado
class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario

    #El método getters
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_salario(self):
        return self.__salario

    #Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_salario(self, salario):
        self.__salario = salario

    def insertar_empleado(self, db_connection):
        cursor = db_connection.cursor()
        query = "INSERT INTO empleados (nombre, apellido, salario) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.__nombre, self.__apellido, self.__salario))
        db_connection.commit()
        cursor.close()
        print("Empleado agregado con éxito.")

    @staticmethod
    def mostrar_empleados(db_connection):
        cursor = db_connection.cursor()
        cursor.execute("SELECT id, nombre, apellido, salario FROM empleados")
        empleados = cursor.fetchall()
        print("\nLista de empleados:")
        for emp in empleados:
            id_empleado, nombre, apellido, salario = emp
            print(f"ID: {id_empleado}, Nombre: {nombre} {apellido}, Salario: ${salario:,.2f} CLP")
        cursor.close()

    def actualizar_empleado(self, db_connection, id_empleado):
        cursor = db_connection.cursor()
        query = "UPDATE empleados SET nombre = %s, apellido = %s, salario = %s WHERE id = %s"
        cursor.execute(query, (self.__nombre, self.__apellido, self.__salario, id_empleado))
        db_connection.commit()
        cursor.close()
        print("Empleado actualizado con éxito.")

    def borrar_empleado(self, db_connection, id_empleado):
        cursor = db_connection.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        cursor.execute(query, (id_empleado,))
        db_connection.commit()
        cursor.close()
        print("Empleado borrado con éxito.")

    @staticmethod
    def calcular_gastos_salarios(db_connection):
        cursor = db_connection.cursor()
        cursor.execute("SELECT SUM(salario) FROM empleados")
        total_gastos = cursor.fetchone()[0]
        cursor.close()
        return total_gastos if total_gastos is not None else 0.0

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, apellido, salario, antiguedad):
        super().__init__(nombre, apellido, salario)
        self.__antiguedad = antiguedad

    def get_antiguedad(self):
        return self.__antiguedad

    def set_antiguedad(self, antiguedad):
        self.__antiguedad = antiguedad

    def get_salario(self):
        aumento = self.__antiguedad * 0.05 * self.get_salario()  # 5% por año
        return self.get_salario() + aumento

class JefeDeProyecto(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido, salario)
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def mostrar_tareas(self):
        print("\nTareas del proyecto:")
        for tarea in self.tareas:
            print(f"- {tarea}")

    def enviar_informe(self, mensaje, destinatario="erick.bailey@inacapmail.cl"):
        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            email_user = "diego.ibanez15@inacapmail.cl"  #Cambiar el correo
            email_password = "contraseña123"  #Cambiar la contraseña

            msg = MIMEText(mensaje)
            msg['Subject'] = 'Informe de Proyecto'
            msg['From'] = email_user
            msg['To'] = destinatario

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_user, email_password)
                server.send_message(msg)

            print("Informe enviado con éxito.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")

    def generar_documentacion(self, contenido):
        with open("documentacion_proyecto.txt", "w") as archivo:
            archivo.write(contenido)
        print("Documentación generada con éxito.")

    def crear_repositorio(self, nombre_repo):
        os.makedirs(nombre_repo, exist_ok=True)
        print(f"Repositorio '{nombre_repo}' creado.")

    def manejar_merge(self, nombre_repo):
        print(f"Merge realizado en el repositorio '{nombre_repo}'.")

# Ejemplo de uso:
if __name__ == "__main__":
    db_connection = mysql.connector.connect(
        host='localhost',  #Cambiar este apartado si es necesario
        user='usuario_empleados',  #El nombre de usuario
        password='',  #La contraseña de MySQL (Se deja vacío si no hay)
        database='gestion_empleados'  #Nombre de la base de datos
    )

    #Datos de empleados para la base de datos
    empleados_data = [
        ("Diego", "Ibáñez", 500000), 
        ("Sofía", "Mendoza", 600000),
        ("Lucas", "Castillo", 700000),
        ("Valentina", "Morales", 550000),
        ("Mateo", "Torres", 650000),
        ("Isabella", "Rojas", 720000),  #Datos de los empleados
    ]

    for nombre, apellido, salario in empleados_data:
        empleado = Empleado(nombre, apellido, salario)
        empleado.insertar_empleado(db_connection)

    # Creación y uso del jefe de proyecto
    jefe = JefeDeProyecto("Carlos", "Sánchez", 6000000)
    jefe.agregar_tarea("Definir requerimientos")
    jefe.agregar_tarea("Diseñar arquitectura del sistema")
    jefe.mostrar_tareas()
    
    jefe.generar_documentacion("Documentación del proyecto...")
    jefe.enviar_informe("Este es un informe de avances del proyecto.")
    jefe.crear_repositorio("Repositorio_Proyecto")
    jefe.manejar_merge("Repositorio_Proyecto")
