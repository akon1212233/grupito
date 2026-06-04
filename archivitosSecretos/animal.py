# resources/classes/animal.py
from database.conexion import conexion
from resources.classes.usuarios import usuario

class animal:
    def __init__(self, raza: str, dueño: usuario, edad: int, nombreAnimal: str, genero: str, id_mascota: int = None):
        self.id_mascota = id_mascota
        self.raza = raza
        self.edad = edad 
        self.nombreAnimal = nombreAnimal
        self.genero = genero
        self.dueño = dueño              

    @staticmethod
    def crear_en_bd(nombre, raza_id, sexo_id):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mascotas (nombre_mascota, id_raza, id_sexo_mascota) VALUES (%s, %s, %s)", (nombre, raza_id, sexo_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def ver_todos():
        conn = conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT m.id_mascota, m.nombre_mascota, r.nombre_raza, s.tipo_sexo_mascota 
            FROM mascotas m 
            INNER JOIN razas r ON m.id_raza = r.id_raza 
            INNER JOIN sexos_mascotas s ON m.id_sexo_mascota = s.id_sexo_mascota 
            WHERE m.deleted = 0
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def actualizar_nombre(id_masc, nuevo_nom):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE mascotas SET nombre_mascota = %s WHERE id_mascota = %s", (nuevo_nom, id_masc))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar_logico(id_masc):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE mascotas SET deleted = 1 WHERE id_mascota = %s", (id_masc,))
        conn.commit()
        cursor.close()
        conn.close()
