# CRUD
from conexion import Conexion
class Procesos:
    
    def __init__(self, tipoEstado, estado, solicitud):
        self.tipoEstado = tipoEstado
        self.estado = estado
        self.solicitud = solicitud
    

    def ingresoProceso():
        
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        

        pass



#Aca va la tablas tipo,estado,solicitudes


