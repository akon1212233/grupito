from conexion import Conexion
from classes.animal import Animales
from classes.ubicacion import Ubicaciones
from classes.proceso import Procesos
from classes.usuario import Usuarios
#      MENU WHILE
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
                Usuarios.ingresarUsuario()
                pass
            elif segundaOpcion == 2:
                pass
            elif segundaOpcion == 3:
                pass
            elif segundaOpcion == 4:
                pass
            elif segundaOpcion == 0:
                continuar2 == False
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
                pass
            elif segundaOpcion == 2:
                pass
            elif segundaOpcion == 3:
                pass
            elif segundaOpcion == 4:
                pass
            elif segundaOpcion == 0:
                continuar2 == False
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
                pass
            elif segundaOpcion == 2:
                pass
            elif segundaOpcion == 3:
                pass
            elif segundaOpcion == 4:
                pass
            elif segundaOpcion == 0:
                continuar2 == False
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
                pass
            elif segundaOpcion == 2:
                pass
            elif segundaOpcion == 3:
                pass
            elif segundaOpcion == 4:
                pass
            elif segundaOpcion == 0:
                continuar2 == False
            else:
                print("Opcion no valida")
    elif primeraOpcion == 0:
        continuar = False
        print("\n\n Adios!")
    else:
        print("Opcion no valida")
