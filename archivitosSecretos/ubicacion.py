# resources/classes/ubicacion.py
from database.conexion import conexion

class ubicacion:
    def __init__(self, calle: str, numero: str, comuna: str, region: str, depto: str = None, id_direccion: int = None):
        self.id_direccion = id_direccion
        self.calle = calle
        self.numero = numero
        self.departamento = depto
        self.comuna = comuna    
        self.region = region    

    @staticmethod
    def crear_en_bd(calle, numero, id_comuna):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO direcciones (calle, numero, id_comuna) VALUES (%s, %s, %s)", (calle, numero, id_comuna))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def ver_todos():
        conn = conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT d.id_direccion, d.calle, d.numero, c.nombre_comuna 
            FROM direcciones d 
            INNER JOIN comunas c ON d.id_comuna = c.id_comuna 
            WHERE d.deleted = 0
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def actualizar_calle(id_dir, nueva_calle):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE direcciones SET calle = %s WHERE id_direccion = %s", (nueva_calle, id_dir))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar_logico(id_dir):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE direcciones SET deleted = 1 WHERE id_direccion = %s", (id_dir,))
        conn.commit()
        cursor.close()
        conn.close()
