# CRUD
from conexion import Conexion

class Procesos:

    def __init__(self, id_mascota: int, id_adoptante: int, id_empleado: int, id_estado: int, fecha_solicitud: str):
        self.id_mascota = id_mascota
        self.id_adoptante = id_adoptante
        self.id_empleado = id_empleado
        self.id_estado = id_estado
        self.fecha_solicitud = fecha_solicitud

    def ingresarProceso(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO solicitudes_adopciones (id_mascota, id_adoptante, id_empleado, id_estado, fecha_solicitud)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            self.id_mascota,
            self.id_adoptante,
            self.id_empleado,
            self.id_estado,
            self.fecha_solicitud
        )

        cursor.execute(sql, valores)
        conexion.commit()
        print("\nProceso de adopción ingresado correctamente!\n")

        cursor.close()
        conexion.close()

    @staticmethod
    def verProcesos():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT
                sa.id_solicitud_adopcion,
                m.nombre_mascota,
                CONCAT(pa.nombre, ' ', pa.apellido) AS adoptante,
                CONCAT(pe.nombre, ' ', pe.apellido) AS empleado,
                e.nombre_estado,
                sa.fecha_solicitud
            FROM solicitudes_adopciones sa
            INNER JOIN mascotas m ON sa.id_mascota = m.id_mascota
            INNER JOIN adoptantes a ON sa.id_adoptante = a.id_adoptante
            INNER JOIN personas pa ON a.id_persona = pa.id_persona
            LEFT JOIN empleados em ON sa.id_empleado = em.id_empleado
            LEFT JOIN personas pe ON em.id_persona = pe.id_persona
            INNER JOIN estados e ON sa.id_estado = e.id_estado
            WHERE sa.deleted = 0
        """

        cursor.execute(sql)
        procesos = cursor.fetchall()

        print("\n===== Procesos de Adopción =====\n")
        for proceso in procesos:
            empleado = proceso[3] if proceso[3] else "Sin asignar"
            print(
                f"ID: {proceso[0]} | "
                f"Mascota: {proceso[1]} | "
                f"Adoptante: {proceso[2]} | "
                f"Empleado: {empleado} | "
                f"Estado: {proceso[4]} | "
                f"Fecha: {proceso[5]}"
            )

        cursor.close()
        conexion.close()

    def actualizar(self):
        id_solicitud = input("Ingrese ID del proceso a modificar: ")

        print("\n¿Qué desea modificar?")
        print("1. Estado")
        print("2. Empleado asignado")
        print("3. Fecha de solicitud")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Procesos.verEstados()
            nuevo_valor = input("Ingrese el ID del nuevo estado: ")
            campo = "id_estado"
        elif opcion == "2":
            nuevo_valor = input("Ingrese el ID del nuevo empleado: ")
            campo = "id_empleado"
        elif opcion == "3":
            nuevo_valor = input("Ingrese la nueva fecha (YYYY-MM-DD): ").strip()
            campo = "fecha_solicitud"
        else:
            print("Opción no válida.")
            return

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = f"UPDATE solicitudes_adopciones SET {campo} = %s WHERE id_solicitud_adopcion = %s"
        cursor.execute(sql, (nuevo_valor, id_solicitud))
        conexion.commit()
        print(f"\nProceso actualizado correctamente.")

        cursor.close()
        conexion.close()

    def eliminar(self):
        id_solicitud = input("Ingrese ID del proceso a eliminar: ")
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = "UPDATE solicitudes_adopciones SET deleted = 1 WHERE id_solicitud_adopcion = %s"

        cursor.execute(sql, (id_solicitud,))
        conexion.commit()
        print("\nProceso eliminado correctamente.")

        cursor.close()
        conexion.close()

    @staticmethod
    def verEstados():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT id_estado, nombre_estado
            FROM estados
            WHERE deleted = 0
        """
        cursor.execute(sql)
        estados = cursor.fetchall()

        print("\n--- Estados disponibles ---")
        for estado in estados:
            print(f"  [{estado[0]}] {estado[1]}")

        cursor.close()
        conexion.close()