class animal:
    def __init__(self, raza:str, dueño:usuario, edad:int, nombreAnimal:str, genero:str):
        self.raza = raza
        self.dueño = dueño
        self.edad = edad 
        self.nombreAnimal = nombreAnimal
        self.genero = genero
#Aca va las tablas tipo,raza,genero animal,mascotas

class usuario:

    def __init__(self, tipoUsuario:int,username,nombre,email,contraseña,rut,telefono,nacimiento,ubicacion:ubicacion):
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

class proceso:
    pass
#Aca va la tablas tipo,estado,solicitudes

















 