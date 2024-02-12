import database


con = database.Database()

while True:
    print("1. Agregar una tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar una tarea como completada")
    print("4. Eliminar una tarea")
    print("5. Salir")

    option = input("Ingrese su acción: ")

    if option == "1":
        name = input("Ingrese nombre de tarea: ")
        desc = input("Ingrese su descripción: ")
        con.add(name, desc)
        print("Guardado exitosamente")
    elif option == "2":
        data = con.show()
        for (_id, name, desc,complted) in data:
            _complted = "Completada" if complted else "Incompleta"
            print(f"{_id} {name} {desc} { _complted } \n")
    elif option == "3":
        _id = input("Ingrese indice de tarea: ")
        con.completed(_id)
    elif option == "4":
        _id = input("Ingrese indice de tarea: ")
        con.delete(_id)
    elif option == "5":
        break
    else:
        break