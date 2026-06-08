from conexion import Conexion
from classes.usuario import Usuarios

class Animales:
    def __init__(self, raza: str, dueño: Usuarios, edad: int, nombreAnimal: str, genero: str):
        self.raza = raza
        self.dueño = dueño
        self.edad = edad
        self.nombreAnimal = nombreAnimal
        self.genero = genero

    def anadirAnimal(self):
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO mascotas (nombre_mascota, id_raza, id_sexo_mascota, id_usuario)
            SELECT %s,
                (SELECT id_raza FROM razas WHERE nombre_raza = %s),
                (SELECT id_sexo_mascota FROM sexos_mascotas WHERE tipo_sexo_mascota = %s),
                %s
        """
        valores = (
            self.nombreAnimal,
            self.raza,
            self.genero,
            self.dueño
        )

        cursor.execute(sql, valores)
        conexion.commit()
        print("\nAnimal añadido\n")

        cursor.close()
        conexion.close()

    @staticmethod
    def verAnimales():
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT
                m.nombre_mascota,
                r.nombre_raza,
                s.tipo_sexo_mascota,
                p.nombre,
                p.apellido
            FROM mascotas m
            INNER JOIN razas r ON m.id_raza = r.id_raza
            INNER JOIN sexos_mascotas s ON m.id_sexo_mascota = s.id_sexo_mascota
            LEFT JOIN solicitudes_adopciones sa ON m.id_mascota = sa.id_mascota
                AND sa.id_estado = (SELECT id_estado FROM estados WHERE nombre_estado = 'Aprobada')
            LEFT JOIN adoptantes a ON sa.id_adoptante = a.id_adoptante
            LEFT JOIN personas p ON a.id_persona = p.id_persona
            WHERE m.deleted = 0
        """

        cursor.execute(sql)
        animales = cursor.fetchall()

        print("\n===== Animales Registrados =====\n")
        for animal in animales:
            dueño = f"{animal[3]} {animal[4]}" if animal[3] else "Sin adoptante"
            print(
                f"Nombre: {animal[0]} | "
                f"Raza: {animal[1]} | "
                f"Sexo: {animal[2]} | "
                f"Adoptante: {dueño}"
            )

        cursor.close()
        conexion.close()

    def actualizar(self):
        id_mascota = input("Ingrese ID de la mascota a modificar: ")

        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        opcion = input("Seleccione una opción: ")

        campos = {"1": "nombre_mascota"}

        if opcion not in campos:
            print("Opción no válida.")
            return

        campo = campos[opcion]
        nuevo_valor = input(f"Ingrese el nuevo {campo}: ").strip()

        if campo == "nombre_mascota":
            self.nombreAnimal = nuevo_valor

        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = f"UPDATE mascotas SET {campo} = %s WHERE id_mascota = %s"
        cursor.execute(sql, (nuevo_valor, id_mascota))
        conexion.commit()
        print(f"\n{campo.capitalize()} actualizado correctamente.")

        cursor.close()
        conexion.close()

    def eliminar(self):
        id_mascota = input("Ingrese ID de la mascota: ")
        conexion = Conexion.conexion()
        cursor = conexion.cursor()

        sql = "UPDATE mascotas SET deleted = 1 WHERE id_mascota = %s"

        cursor.execute(sql, (id_mascota,))
        conexion.commit()
        print("\nAnimal eliminado correctamente.")

        cursor.close()
        conexion.close()