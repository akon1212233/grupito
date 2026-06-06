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
                    u.username,
                    p.nombre,
                    t.id_tipo_usuario,
                    t.nombre_tipo_usuario
            from usuarios u
            inner join tipo_usuarios t 
            on u.id_tipo_usuario = t.id_tipo_usuario
            inner join personas p
            on u.id_persona = p.id_persona
            where u.deleted = 0 and t.deleted = 0 and p.deleted = 0;
            
        
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()
        print("\n===== Usuarios =====\n")
        for usuario in usuarios:
            print(
                f"Username: {usuario[0]} | "
                f"Nombre: {usuario[1]} | "
                f"Rol: {usuario[2]} |" 
                f"Nombre del Rol {usuario[3]}"
            )

        cursor.close()
        conexion.close()
        





