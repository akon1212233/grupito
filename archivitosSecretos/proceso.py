# resources/classes/procesos.py
from database.conexion import conexion

class proceso:
    def __init__(self, id_solicitud: int = None, id_mascota: int = None, id_adoptante: int = None, id_estado: int = None):
        self.id_solicitud = id_solicitud
        self.id_mascota = id_mascota
        self.id_adoptante = id_adoptante
        self.id_estado = id_estado

    @staticmethod
    def crear_en_bd(id_m, id_a, id_e, id_est, fecha):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO solicitudes_adopciones (id_mascota, id_adoptante, id_empleado, id_estado, fecha_solicitud) 
            VALUES (%s, %s, %s, %s, %s)
        """, (id_m, id_a, id_e, id_est, fecha))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def ver_todos():
        conn = conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT s.id_solicitud_adopcion, m.nombre_mascota, p.nombre AS adoptante, e.nombre_estado 
            FROM solicitudes_adopciones s 
            INNER JOIN mascotas m ON s.id_mascota = m.id_mascota 
            INNER JOIN adoptantes a ON s.id_adoptante = a.id_adoptante 
            INNER JOIN personas p ON a.id_persona = p.id_persona 
            INNER JOIN estados e ON s.id_estado = e.id_estado 
            WHERE s.deleted = 0
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def actualizar_estado(id_sol, nuevo_est):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE solicitudes_adopciones SET id_estado = %s WHERE id_solicitud_adopcion = %s", (nuevo_est, id_sol))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar_logico(id_sol):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE solicitudes_adopciones SET deleted = 1 WHERE id_solicitud_adopcion = %s", (id_sol,))
        conn.commit()
        cursor.close()
        conn.close()
