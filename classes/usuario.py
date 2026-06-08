from conexion import Conexion
from classes.ubicacion import Ubicaciones

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
            VALUES (%s, %s, %s, %s, %s)
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
            (username, password_hash, email, id_persona, id_tipo_usuario)
            VALUES (%s, %s, %s, %s, %s)
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
                t.nombre_tipo,
                d.calle,
                d.numero,
                c.nombre_comuna
            FROM usuarios u
            INNER JOIN tipos_usuarios t ON u.id_tipo_usuario = t.id_tipo_usuario
            INNER JOIN personas p ON u.id_persona = p.id_persona
            LEFT JOIN empleados e ON p.id_persona = e.id_persona
            LEFT JOIN adoptantes ad ON p.id_persona = ad.id_persona
            LEFT JOIN direcciones d ON COALESCE(e.id_direccion, ad.id_direccion) = d.id_direccion
            LEFT JOIN comunas c ON d.id_comuna = c.id_comuna
            WHERE u.deleted = 0 AND t.deleted = 0 AND p.deleted = 0
        """

        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        print("\n===== Usuarios Activos =====\n")
        for usuario in usuarios:
            direccion = f"{usuario[4]} {usuario[5]}, {usuario[6]}" if usuario[4] else "Sin dirección"
            print(
                f"Username: {usuario[0]} | "
                f"Nombre: {usuario[1]} {usuario[2]} | "
                f"Rol: {usuario[3]} | "
                f"Dirección: {direccion}"
            )

        cursor.close()
        conexion.close()

    def actualizar(self):
        id_persona = input("Ingrese ID de la persona que quiere modificar: ")

        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Teléfono")
        print("4. Email")
        opcion = input("Seleccione una opción: ")

        opciones = {
            "1": ("nombre",   "personas"),
            "2": ("apellido", "personas"),
            "3": ("telefono", "personas"),
            "4": ("email",    "usuarios"),
        }

        if opcion not in opciones:
            print("Opción no válida.")
            return

        campo, tabla = opciones[opcion]
        nuevo_valor = input(f"Ingrese el nuevo {campo}: ").strip()

        if campo == "nombre":
            self.nombre = nuevo_valor
        elif campo == "apellido":
            self.apellido = nuevo_valor
        elif campo == "telefono":
            self.telefono = nuevo_valor
        elif campo == "email":
            self.email = nuevo_valor

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = f"UPDATE {tabla} SET {campo} = %s WHERE id_persona = %s"
        cursor.execute(sql, (nuevo_valor, id_persona))
        conexion.commit()
        print(f"\n{campo.capitalize()} actualizado correctamente.")

        cursor.close()
        conexion.close()

    def eliminar(self):
        id_usuario = input("Ingrese ID del usuario: ")
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET deleted = 1
        WHERE id_usuario = %s
        """

        cursor.execute(sql, (id_usuario,))
        conexion.commit()
        print("\nUsuario eliminado correctamente.")

        cursor.close()
        conexion.close()