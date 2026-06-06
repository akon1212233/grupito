# CRUD
from conexion import Conexion


class Ubicaciones:
    def __init__(self, departamento, comuna, calle, numero):
        self.departamento = departamento
        self.comuna = comuna
        self.calle = calle
        self.numero = numero
        
    
    def direccion(self):

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            insert into direciones
            (
                id_comuna,
                calle,
                numero,
                departamento
            )
            values (
                %s,
                %s,
                %s,
                %s
            )
            """
        
        valores = (
            self.departamento,
            self.comuna,
            self.calle,
            self.numero
        )


        cursor.execute(sql, valores)

        cursor.commit()
        print("\nUbicación guardada\n")
        cursor.close()
        conexion.close()

        @staticmethod
        def mostrarUbicacion():
            pass


