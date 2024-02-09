# Sistema de Registro de Usuarios
class User: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Auth:
    __users = []
    def register(self, user):
        self.__users.append(user)
        print("Usuario registrado exitosamente.")

    def login(self, data):
        for user in self.__users:
           if user.username == data.username and user.password == data.password:
                print("Inicio de sesión correcto.")
                print(f"Bienvenido {data.username}")
                return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False
# Crear una instancia de Auth fuera del bucle principal
auth = Auth()

# Menú principal
while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        username = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        user = User(username, password)
        auth.register(user)
    elif opcion == "2":
        username = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        user = User(username, password)
        if not auth.login(user):
            print("Inicio de sesión no válido.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("La opción sumistrada no es valida.")
        break