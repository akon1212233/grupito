# CRUD
from conexion import Conexion


class Ubicaciones:
    def __init__(self, region, comuna, calle, numero):
        self.region = region
        self.comuna = comuna
        self.calle = calle
        self.numero = numero
        
    
    def direccion(self):

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            insert into
            (
                region
                comuna
                calle
                numero
            )
            values (
                %s,
                %s,
                %s,
                %s
            )
            """
        
        valores = (
            self.region,
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


