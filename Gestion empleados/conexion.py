import mysql.connector

#Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",  # Cambiar esto si el host es diferente
    user="usuario_empleados",  # nombre de usuario
    password="",  # este apartado dejar vacío si no hay contraseña
    database="gestion_empleados"  # El nombre de la base de datos
)

#  Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error en la conexión")

#Funciones CRUD
def insertar_empleado(nombre, apellido, salario):
    cursor = conexion.cursor()
    sql = "INSERT INTO empleados (nombre, apellido, salario) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, salario))
    conexion.commit()
    cursor.close()
    print("Empleado insertado con éxito")

def obtener_empleados():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    return empleados

def actualizar_empleado(id_empleado, nombre, apellido, salario):
    cursor = conexion.cursor()
    sql = "UPDATE empleados SET nombre = %s, apellido = %s, salario = %s WHERE id = %s"
    cursor.execute(sql, (nombre, apellido, salario, id_empleado))
    conexion.commit()
    cursor.close()
    print("Empleado actualizado con éxito")

def borrar_empleado(id_empleado):
    cursor = conexion.cursor()
    sql = "DELETE FROM empleados WHERE id = %s"
    cursor.execute(sql, (id_empleado,))
    conexion.commit()
    cursor.close()
    print("Empleado borrado con éxito")

#Un ejemplo de uso
if conexion.is_connected():
    #Insertar un nuevo empleado
    insertar_empleado('Diego', 'Ibáñez', 500000)

    #Obtener y mostrar todos los empleados
    empleados = obtener_empleados()
    for emp in empleados:
        print(emp)

    # Actualizar un empleado (por ejemplo, el primero)
    actualizar_empleado(1, 'Diego', 'Ibáñez', 600000)

    #  Borrar un empleado (por ejemplo, el primero)
    borrar_empleado(1)

#Cerrar la conexión
conexion.close()