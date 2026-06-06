from conexion import Conexion
from ubicacion import Ubicaciones
# CRUD
class Usuarios:

    def __init__(self, tipoUsuario:int,username,nombre,email,contraseña,rut,telefono,nacimiento,ubicacion:Ubicaciones):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.rut = rut
        self.telefono = telefono
        self.nacimiento = nacimiento
        self.username = username
        self.tipoUsuario = tipoUsuario
        self.ubicacion = ubicacion
#Aca va las tablas personas,empleados,adoptantes,tipoUsuario,usuario

    def ingresarUsuario(self):
        
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            insert into
            ( 
                tipoUsuario, 
                username, 
                nombre, 
                email, 
                contraseña, 
                rut, 
                telefono, 
                nacimiento, 
                ubicacion_id
            )

            values 
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """
        valores = (
            self.tipoUsuario,
            self.username,
            self.nombre,
            self.email,
            self.contraseña,
            self.rut,
            self.telefono,
            self.nacimiento,
            self.ubicacion
        )

        cursor.execute(sql, valores)

        cursor.commit()
        print("\nUsuario ingresado\n")
        cursor.close()
        conexion.close()

    @staticmethod
    def mostrarActvivos():

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """

            select
                    username
                    nombre
                    tipoUsuario
            from usuarios
            where deleted = 0
            order by usuarios ASC;
        
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()
        print("\n===== Usuarios =====\n")
        for usuario in usuarios:
            print(
                f"Username: {usuario[0]} | "
                f"Nombre: {usuario[1]} | "
                f"Rol: {usuario[2]}"
            )

        cursor.close()
        conexion.close()
        





