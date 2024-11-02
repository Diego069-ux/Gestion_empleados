import mysql.connector

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_salario(self):
        return self.__salario

    # Métodos setters
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
        # Ejemplo simple de cálculo de salario considerando antigüedad
        aumento = self.__antiguedad * 0.05 * self._Empleado__salario  # 5% por año
        return self._Empleado__salario + aumento