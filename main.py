from conexion import Conexion
from classes.animal import Animales
from classes.ubicacion import Ubicaciones
from classes.proceso import Procesos
from classes.usuario import Usuarios
from helpers import verTiposUsuario, verRazas, verAdoptantes, verEmpleados, verComunas, verUsuarios, verMascotas

continuar = True
continuar2 = False

while continuar:
    print("""
    ============================
    1) Ingresar   (CREATE)
    2) Ver        (READ)
    3) Actualizar (UPDATE)
    4) Eliminar   (DELETE)
    0) Salir
    ============================
    """)
    primeraOpcion = int(input("Seleccione una operación (0-4): "))

    if primeraOpcion == 1:
        continuar2 = True
        while continuar2:
            print("""
    ============================
              (CREAR)
    ============================
    1) Ingresar Usuario
    2) Ingresar Animal
    3) Ingresar Ubicacion
    4) Ingresar Proceso
    0) Salir
    ============================
            """)
            segundaOpcion = int(input("Seleccione: "))
            if segundaOpcion == 1:
                verTiposUsuario()
                tipoUsuario = int(input("Tipo de usuario (ID): "))
                username   = input("Username: ")
                nombre     = input("Nombre: ")
                apellido   = input("Apellido: ")
                email      = input("Email: ")
                contraseña = input("Contraseña: ")
                rut        = input("RUT: ")
                telefono   = input("Teléfono: ")
                nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                u = Usuarios(tipoUsuario, username, nombre, apellido, email, contraseña, rut, telefono, nacimiento)
                u.ingresarUsuario()
            elif segundaOpcion == 2:
                nombreAnimal = input("Nombre del animal: ")
                verRazas()
                raza   = input("Raza: ")
                genero = input("Sexo (Macho/Hembra): ")
                edad   = int(input("Edad: "))
                verUsuarios()
                dueño  = int(input("ID del usuario dueño: "))
                a = Animales(raza, dueño, edad, nombreAnimal, genero)
                a.anadirAnimal()
            elif segundaOpcion == 3:
                verComunas()
                comuna       = input("Comuna: ")
                calle        = input("Calle: ")
                numero       = input("Número: ")
                departamento = input("Departamento (dejar vacío si no aplica): ") or None
                ub = Ubicaciones(comuna, calle, numero, departamento)
                ub.guardar()
            elif segundaOpcion == 4:
                verAdoptantes()
                id_adoptante = int(input("ID del adoptante: "))
                verEmpleados()
                id_empleado  = int(input("ID del empleado: "))
                verMascotas()
                id_mascota   = int(input("ID de la mascota: "))
                Procesos.verEstados()
                id_estado       = int(input("ID del estado: "))
                fecha_solicitud = input("Fecha de solicitud (YYYY-MM-DD): ")
                p = Procesos(id_mascota, id_adoptante, id_empleado, id_estado, fecha_solicitud)
                p.ingresarProceso()
            elif segundaOpcion == 0:
                continuar2 = False
            else:
                print("Opcion no valida")

    elif primeraOpcion == 2:
        continuar2 = True
        while continuar2:
            print("""
    ============================
               (VER)
    ============================
    1) Ver Usuarios
    2) Ver Animales
    3) Ver Ubicaciones
    4) Ver Procesos
    0) Salir
    ============================
            """)
            segundaOpcion = int(input("Seleccione: "))
            if segundaOpcion == 1:
                Usuarios.mostrarActivos()
            elif segundaOpcion == 2:
                Animales.verAnimales()
            elif segundaOpcion == 3:
                Ubicaciones.mostrarUbicaciones()
            elif segundaOpcion == 4:
                Procesos.verProcesos()
            elif segundaOpcion == 0:
                continuar2 = False
            else:
                print("Opcion no valida")

    elif primeraOpcion == 3:
        continuar2 = True
        while continuar2:
            print("""
    ============================
            (MODIFICAR)
    ============================
    1) Modificar Usuarios
    2) Modificar Animales
    3) Modificar Ubicaciones
    4) Modificar Procesos
    0) Salir
    ============================
            """)
            segundaOpcion = int(input("Seleccione: "))
            if segundaOpcion == 1:
                Usuarios.mostrarActivos()
                u = Usuarios(None, None, None, None, None, None, None, None, None)
                u.actualizar()
            elif segundaOpcion == 2:
                Animales.verAnimales()
                a = Animales(None, None, None, None, None)
                a.actualizar()
            elif segundaOpcion == 3:
                Ubicaciones.mostrarUbicaciones()
                ub = Ubicaciones(None, None, None)
                ub.actualizar()
            elif segundaOpcion == 4:
                Procesos.verProcesos()
                p = Procesos(None, None, None, None, None)
                p.actualizar()
            elif segundaOpcion == 0:
                continuar2 = False
            else:
                print("Opcion no valida")

    elif primeraOpcion == 4:
        continuar2 = True
        while continuar2:
            print("""
    ============================
             (ELIMINAR)
    ============================
    1) Eliminar Usuarios
    2) Eliminar Animales
    3) Eliminar Ubicaciones
    4) Eliminar Procesos
    0) Salir
    ============================
            """)
            segundaOpcion = int(input("Seleccione: "))
            if segundaOpcion == 1:
                Usuarios.mostrarActivos()
                u = Usuarios(None, None, None, None, None, None, None, None, None)
                u.eliminar()
            elif segundaOpcion == 2:
                Animales.verAnimales()
                a = Animales(None, None, None, None, None)
                a.eliminar()
            elif segundaOpcion == 3:
                Ubicaciones.mostrarUbicaciones()
                ub = Ubicaciones(None, None, None)
                ub.eliminar()
            elif segundaOpcion == 4:
                Procesos.verProcesos()
                p = Procesos(None, None, None, None, None)
                p.eliminar()
            elif segundaOpcion == 0:
                continuar2 = False
            else:
                print("Opcion no valida")

    elif primeraOpcion == 0:
        continuar = False
        print("\n\n Adios!")
    else:
        print("Opcion no valida")