from conexion import Conexion

class Ubicaciones:
    def __init__(self, comuna, calle, numero, departamento=None):
        self.comuna = comuna
        self.calle = calle
        self.numero = numero
        self.departamento = departamento
        
    def guardar(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO direcciones (calle, numero, departamento, id_comuna)
            SELECT %s, %s, %s, id_comuna 
            FROM comunas 
            WHERE nombre_comuna = %s
        """
        valores = (self.calle, self.numero, self.departamento, self.comuna)
        
        cursor.execute(sql, valores)
        conexion.commit()
        print("\nUbicación guardada\n")
        
        cursor.close()
        conexion.close()

    @staticmethod
    def mostrarUbicaciones():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT d.calle, d.numero, d.departamento, c.nombre_comuna
            FROM direcciones d
            INNER JOIN comunas c ON d.id_comuna = c.id_comuna
            WHERE d.deleted = 0 and c.deleted = 0;
        """

        cursor.execute(sql)
        direcciones = cursor.fetchall()
        
        print("\n===== Ubicaciones Registradas =====\n")
        for dir in direcciones:
            print(f"Calle: {dir[0]} {dir[1]} | Depto: {dir[2]} | Comuna: {dir[3]}")

        cursor.close()
        conexion.close()