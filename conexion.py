import mysql.connector

class Conexion:
    @staticmethod
    def conexion():    
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "adopcionMascotas",
        )
        return conexion