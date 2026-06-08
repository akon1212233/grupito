from conexion import Conexion

def verTiposUsuario():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_tipo_usuario, nombre_tipo FROM tipos_usuarios WHERE deleted = 0")
    tipos = cursor.fetchall()
    print("\n--- Tipos de usuario ---")
    for t in tipos:
        print(f"  [{t[0]}] {t[1]}")
    cursor.close()
    conexion.close()

def verRazas():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_raza, nombre_raza FROM razas WHERE deleted = 0")
    razas = cursor.fetchall()
    print("\n--- Razas disponibles ---")
    for r in razas:
        print(f"  [{r[0]}] {r[1]}")
    cursor.close()
    conexion.close()

def verAdoptantes():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT a.id_adoptante, p.nombre, p.apellido
        FROM adoptantes a
        INNER JOIN personas p ON a.id_persona = p.id_persona
        WHERE a.deleted = 0
    """)
    adoptantes = cursor.fetchall()
    print("\n--- Adoptantes disponibles ---")
    for a in adoptantes:
        print(f"  [{a[0]}] {a[1]} {a[2]}")
    cursor.close()
    conexion.close()

def verEmpleados():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT e.id_empleado, p.nombre, p.apellido, e.cargo
        FROM empleados e
        INNER JOIN personas p ON e.id_persona = p.id_persona
        WHERE e.deleted = 0
    """)
    empleados = cursor.fetchall()
    print("\n--- Empleados disponibles ---")
    for e in empleados:
        print(f"  [{e[0]}] {e[1]} {e[2]} - {e[3]}")
    cursor.close()
    conexion.close()

def verComunas():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_comuna, nombre_comuna FROM comunas WHERE deleted = 0")
    comunas = cursor.fetchall()
    print("\n--- Comunas disponibles ---")
    for c in comunas:
        print(f"  [{c[0]}] {c[1]}")
    cursor.close()
    conexion.close()

def verUsuarios():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT u.id_usuario, u.username, p.nombre, p.apellido
        FROM usuarios u
        INNER JOIN personas p ON u.id_persona = p.id_persona
        WHERE u.deleted = 0
    """)
    usuarios = cursor.fetchall()
    print("\n--- Usuarios disponibles ---")
    for u in usuarios:
        print(f"  [{u[0]}] {u[1]} - {u[2]} {u[3]}")
    cursor.close()
    conexion.close()

def verMascotas():
    conexion = Conexion.conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT m.id_mascota, m.nombre_mascota, r.nombre_raza
        FROM mascotas m
        INNER JOIN razas r ON m.id_raza = r.id_raza
        WHERE m.deleted = 0
    """)
    mascotas = cursor.fetchall()
    print("\n--- Mascotas disponibles ---")
    for m in mascotas:
        print(f"  [{m[0]}] {m[1]} - {m[2]}")
    cursor.close()
    conexion.close()