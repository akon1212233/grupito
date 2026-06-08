from conexion import Conexion
from ubicacion import Ubicaciones

class Usuarios:

    def __init__(self, tipoUsuario: int, username: str, nombre: str, apellido: str, 
                email: str, contraseña: str, rut: str, telefono: str, nacimiento: str, 
                ubicacion: Ubicaciones = None):
        
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.rut = rut
        self.telefono = telefono
        self.nacimiento = nacimiento
        self.username = username
        self.tipoUsuario = tipoUsuario
        self.ubicacion = ubicacion

    def ingresarUsuario(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql_persona = """
            INSERT INTO personas (RUT, nombre, apellido, telefono, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores_persona = (
            self.rut,
            self.nombre,
            self.apellido,
            self.telefono,
            self.nacimiento
        )

        cursor.execute(sql_persona, valores_persona)
        
        id_persona_generado = cursor.lastrowid

        sql_usuario = """
            INSERT INTO usuarios 
            (
                username, 
                password_hash,
                email, 
                id_persona, 
                id_tipo_usuario
            )
            VALUES 
            (
                %s, 
                %s, 
                %s,
                %s, 
                %s
            )
        """
        valores_usuario = (
            self.username,
            self.contraseña,
            self.email,
            id_persona_generado,
            self.tipoUsuario
        )

        cursor.execute(sql_usuario, valores_usuario)

        conexion.commit()
        print("\nUsuario y persona ingresado correctamente!\n")
        
        cursor.close()
        conexion.close()

    @staticmethod
    def mostrarActivos():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT 
                u.username,
                p.nombre,
                p.apellido,
                t.nombre_tipo
            FROM usuarios u
            INNER JOIN tipos_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
            INNER JOIN personas p ON u.id_persona = p.id_persona
            WHERE u.deleted = 0 AND t.deleted = 0 AND p.deleted = 0;
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        print("\n===== Usuarios Activos =====\n")
        for usuario in usuarios:
            print(
                f"Username: {usuario[0]} | "
                f"Nombre: {usuario[1]} {usuario[2]} | "
                f"Rol: {usuario[3]}"
            )

        cursor.close()
        conexion.close()

        