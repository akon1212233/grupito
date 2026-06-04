# resources/classes/usuarios.py
from database.conexion import conexion
from resources.classes.ubicacion import ubicacion

class usuario:
    def __init__(self, tipoUsuario: int, username: str, nombre: str, email: str, contraseña: str, 
                 rut: str, telefono: str, nacimiento: str, ubicacion_obj: ubicacion = None, id_persona: int = None):                 
        self.id_persona = id_persona
        self.tipoUsuario = tipoUsuario  
        self.username = username
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.rut = rut
        self.telefono = telefono
        self.nacimiento = nacimiento
        self.ubicacion = ubicacion_obj      

    @staticmethod
    def crear_en_bd(tipo, user, nom, rut, tel, nac):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (RUT, nombre, apellido, telefono, fecha_nacimiento) VALUES (%s, %s, '', %s, %s)", (rut, nom, tel, nac))
        id_per = cursor.lastrowid
        cursor.execute("INSERT INTO usuarios (username, id_persona, id_tipo_usuario) VALUES (%s, %s, %s)", (user, id_per, tipo))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def ver_todos():
        conn = conexion.conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT u.id_usuario, u.username, p.nombre, tu.nombre_tipo 
            FROM usuarios u 
            INNER JOIN personas p ON u.id_persona = p.id_persona 
            INNER JOIN tipos_usuarios tu ON u.id_tipo_usuario = tu.id_tipo_usuario 
            WHERE u.deleted = 0
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos

    @staticmethod
    def actualizar_telefono(id_user, nuevo_tel):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE personas SET telefono = %s 
            WHERE id_persona = (SELECT id_persona FROM usuarios WHERE id_usuario = %s)
        """, (nuevo_tel, id_user))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def eliminar_logico(id_user):
        conn = conexion.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET deleted = 1 WHERE id_usuario = %s", (id_user,))
        conn.commit()
        cursor.close()
        conn.close()
