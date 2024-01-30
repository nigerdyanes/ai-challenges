def contar_vocales(palabra):
    resultado = { "a": 0, "e": 0, "i": 0, "o": 0, "u": 0 }
    palabra_minuscula = palabra.lower()
    for letra in palabra_minuscula:
        if(letra in ('a','e','i','o','u')):
            conteo = palabra_minuscula.count(letra)
            resultado[letra] = conteo
    
    return resultado

entrada = input("Ingrese la palabra: ")
resultado = contar_vocales(entrada)
print(resultado)