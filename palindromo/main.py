def es_palindromo(texto):
    return texto == texto[::-1]

palabra = input("Ingresa su secuencia de caractares: ")
resultado = es_palindromo(palabra)
print(resultado)