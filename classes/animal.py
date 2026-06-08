from conexion import Conexion
from usuario import Usuarios

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
            INSERT INTO mascotas (nombre, edad, id_raza, id_genero, id_usuario)
            SELECT %s, %s,
                (SELECT id_raza FROM razas WHERE nombre_raza = %s),
                (SELECT id_genero FROM generos_animal WHERE nombre_genero = %s),
                %s
        """
        valores = (
            self.nombreAnimal,
            self.edad,
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
                m.nombre,
                m.edad,
                r.nombre_raza,
                g.nombre_genero,
                u.username
            FROM mascotas m
            INNER JOIN razas r ON m.id_raza = r.id_raza
            INNER JOIN generos_animal g ON m.id_genero = g.id_genero
            INNER JOIN usuarios u ON m.id_usuario = u.id_usuario
            WHERE m.deleted = 0
        """

        cursor.execute(sql)
        animales = cursor.fetchall()

        print("\n===== Animales Registrados =====\n")
        for animal in animales:
            print(
                f"Nombre: {animal[0]} | "
                f"Edad: {animal[1]} | "
                f"Raza: {animal[2]} | "
                f"Género: {animal[3]} | "
                f"Dueño: {animal[4]}"
            )

        cursor.close()
        conexion.close()

    def actualizar(self):
        id_mascota = input("Ingrese ID de la mascota a modificar: ")

        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Edad")
        opcion = input("Seleccione una opción: ")

        campos = {"1": "nombre", "2": "edad"}

        if opcion not in campos:
                print("Opción no válida.")
                return

        campo = campos[opcion]
        nuevo_valor = input(f"Ingrese el nuevo {campo}: ").strip()

        if campo == "nombre":
                self.nombreAnimal = nuevo_valor
        elif campo == "edad":
                self.edad = nuevo_valor

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