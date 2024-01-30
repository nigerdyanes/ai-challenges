def invertir_cadena(value):
    cadena_list = list(value)
    cadena_list.reverse()
    return "".join(cadena_list)

cadena = input("Ingrese la cadena a invertir: ")
resultado = invertir_cadena(cadena)
print(f"Cadena: {resultado}")