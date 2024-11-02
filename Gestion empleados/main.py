from empleados import Empleado
import mysql.connector
from mysql.connector import Error

def main():
    #Conectar a la base de datos MySQL
    try:
        db_connection = mysql.connector.connect(
            host='localhost',        # Cambiar este apartado si es necesario
            user='usuario_empleados', #el nombre de usuario
            password='',             #La contraseña de MySQL (Se deja vacío si no hay)
            database='gestion_empleados' #Nombre de la base de datos
        )
        
        if db_connection.is_connected():
            print("Conexión a la base de datos exitosa.")

            while True:
                print("\nMenú:")
                print("1. Agregar empleado")
                print("2. Mostrar empleados")
                print("3. Actualizar empleado")
                print("4. Borrar empleado")
                print("5. Calcular gastos en salarios")
                print("6. Salir")
                
                opcion = input("Selecciona una opción: ")

                if opcion == '1':
                    nombre = input("Ingrese el nombre del empleado: ")
                    apellido = input("Ingrese el apellido del empleado: ")
                    salario = float(input("Ingrese el salario del empleado: "))
                    empleado = Empleado(nombre, apellido, salario)
                    empleado.insertar_empleado(db_connection)  # Método para insertar empleado
                elif opcion == '2':
                    Empleado.mostrar_empleados(db_connection)  # Método para mostrar empleados
                elif opcion == '3':
                    id_empleado = int(input("ID del empleado a actualizar: "))
                    nombre = input("Nuevo nombre: ")
                    apellido = input("Nuevo apellido: ")
                    salario = float(input("Nuevo salario: "))
                    empleado = Empleado(nombre, apellido, salario)
                    empleado.actualizar_empleado(db_connection, id_empleado)  # Método para actualizar empleado
                elif opcion == '4':
                    id_empleado = int(input("ID del empleado a borrar: "))
                    empleado.borrar_empleado(db_connection, id_empleado)  # Método para borrar empleado
                elif opcion == '5':
                    total_gastos = Empleado.calcular_gastos_salarios(db_connection)  # Método para calcular gastos
                    print(f"Total de gastos en salarios: ${total_gastos:,.2f} CLP")
                elif opcion == '6':
                    break
                else:
                    print("Opción no válida.")

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()
            print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    main()