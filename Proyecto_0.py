def main():
    bienvenida()
    print()
    print("Por favor escoga alguno de los siguientes números, \
dependiendo del método de cifrado que desea utilizar")
    continuar = True
    while continuar:
        try:
             print()
             indicación=int(input("Digite '1' para el método de cifrado césar; '2' para\
el cifrado monoalfabético con palabra clave; '3' para el cifrado vigenère; '4' para el \
el cifrado PlayFair; '5' para el cifrado Rail Fence; '6' para el cifrado escítala:  "))
             limpiar_pantalla()
             while indicación not in [1,2,3,4,5,6]:
                 print("Indicación invalida") 
                 indicación = int(input("Digite algún número válido para continuar: "))
                 limpiar_pantalla()
             if indicación == 1:
                 print("Cifrado César")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))

                 texto = input("Digite el texto: ")

                 desplazamiento = int(input("Digite el desplazamiento: "))

                 if selección == 1:
                  resultado = cesarCod(texto, desplazamiento)
                  print("Texto codificado:")
                  print(resultado)
                 else:
                   resultado = cesarDec(texto, desplazamiento)
                   print("Texto decodificado:")
                   print(resultado)
             elif indicación == 2:
                 print("Cifrado Monoalfabético con Palabra Clave")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría monoCod(texto, palabra)
                 else:
                     print("Decodificar") # Acá iría monoDec(texto, palabra)
             elif indicación == 3:
                 print("Cifrado Vigenère")
                 mainVigenere()
                 print()
             elif indicación == 4:
                 print("Cifrado PlayFair")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría playfairCod(texto, palabra)
                 else:
                     print("Decodificar") # Acá iría playfairDec(texto, palabra)
             elif indicación == 5: #Hay que arreglar eso
                 print("Cifrado Rail Fence")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     texto=input("Diguite el texto que desea codificar: ")
                     print (f"Su texto codificado es: {railfenceCod(texto)}")
                 else:
                     print("Decodificar") # Acá iría railfenceDec(texto)
             else:
                 print("Cifrado Escítala")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría escitalaCod(texto, líneas)
                 else:
                     print("Decodificar") # Acá iría escitalaDec(texto, líneas)
        except Exception as e:
            print(f"Error:{e}")
            continuar = False
        continuar = repetir()

def bienvenida():
    """Programa que se encarga de imprimir un mensaje de bienvenidad para introducir al usuario el programa.
    Entradas y restricciones:
    -ninguna
    Salidas: El mensaje de bienvenida."""
    print("Bienvenido al programa de codificacion y decodificacion de mensajes.")
    print("Creado por Luis, Justin, Miranda.")
    print("En este programa hay varios algoritmos, cada uno con una manera unica de codificar o decodificar, dependiendo de las preferencias del usuario.")

def mainVigenere():
    """Subrutina principal del algoritmo del Cifrado Vigenère.
    Entradas y restricciones:
    -Texto a cifrar
    -Palabra clave
    -Opcion
    Salidas: resultado de la codificacion y descodificacion."""
    clave = leerClave()
    opcion = elegirOpcion()
    texto_clave = preparar(clave)
    if opcion == "1":
        mensaje = leerMensaje()
        texto_mensaje = preparar(mensaje)
        texto_codificado = vigenereCod(texto_mensaje, texto_clave)
        print("Texto codificado:", texto_codificado)
    elif opcion == "2":
        mensaje2 = leerMensaje2()
        texto_mensaje2 = preparar(mensaje2)
        texto_decodificado = vigenereDec(texto_mensaje2, texto_clave)
        print("Texto decodificado:", texto_decodificado)

def leerClave():
    """Funcion que lee la palabra clave para codificar o decodificar ingresada por el usuario.
    Entradas y restricciones:
    -texto del usuario
    Salidas: texto ingresado."""
    clave = input("Primero ingrese la palabra clave para codificar o decodificar su mensaje: ")
    while not clave.isalpha():
        print("La palabra clave solo puede contener letras y espacios.")
        clave = input("Ingrese la palabra clave: ")
    return clave

def elegirOpcion():
    print("\n¿Que desea hacer?")
    print("1. Codificar mensaje")
    print("2. Decodificar mensaje")

    opcion = input("Seleccione una opcion (1 o 2): ")

    while opcion not in ["1", "2"]:
        print("Opcion inválida.")
        opcion = input("Seleccione 1 o 2: ")

    return opcion

def leerMensaje():
    """Funcion que lee el texto que se va a codificar.
    Entradas y restricciones:
    -Mensaje a codificar
    Salidas: Mensaje ingresado."""
    mensaje = input("Ingrese el mensaje que quiere codificar. Solo puede contener letra o espacios: ")
    while not esValido(mensaje):
        print("El mensaje solo puede contener letras y espacios.")
        mensaje = input("Ingrese el mensaje: ")
    return mensaje

def esValido(dato):
    """Funcion booleana que dice si la palabra clave y mensaje a codificar o decodificar es valido o no.
    Entradas y restricciones:
    -Mensaje a analizar (debe ser un string)
    Salidas: Si el mensaje es valido o invalido."""
    if type(dato) != str:
        raise Exception("El mensaje debe ser un string.")
    if dato == "":
        return False
    for letra in dato:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúüvwxyz":
            return False
    return True
    
def preparar(dato):
    """Funcion que convierte el texto a minusculas, sustitye acentos y elimina espacios a al inicio y al final.
    Entradas y restricciones:
    -texto a procesar (tiene que ser un string)
    Salidas: texto sin mayúsculas, acentos y espacios."""
    if type(dato) != str:
        raise Exception("Texto debe ser un string.")
    dato = dato.lower()
    dato = dato.strip()
    dato = dato.replace("á", "a")
    dato = dato.replace("é", "e")
    dato = dato.replace("í", "i")
    dato = dato.replace("ó", "o")
    dato = dato.replace("ú", "u")
    dato = dato.replace("ü", "u")
    return dato

def vigenereCod(mensaje, clave):    

    letras_a_numeros = {

       'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,

       'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,

       'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,

       'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26

    }


    numeros_a_letras = {

       0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',

       7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',

       14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',

       21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'

    }


    texto_codificado = ""

    posicion_clave = 0 

    for letra in mensaje:

       


       if letra in letras_a_numeros:

           


           valor_mensaje = letras_a_numeros[letra]

           


           letra_clave_actual = clave[posicion_clave]

           valor_clave = letras_a_numeros[letra_clave_actual]

           


           suma = valor_mensaje + valor_clave

           


           nuevo_valor = suma % 27

           


           nueva_letra = numeros_a_letras[nuevo_valor]

           


           texto_codificado = texto_codificado + nueva_letra

           


           posicion_clave = posicion_clave + 1

           


           if posicion_clave == len(clave):

               posicion_clave = 0

               

       else:
           texto_codificado = texto_codificado + letra

    return texto_codificado

def leerMensaje2():
    """Funcion que lee el texto que se va a decodificar.
    Entradas y restricciones:
    -Mensaje a decodificar
    Salidas: Mensaje ingresado."""
    mensaje2 = input("Ingrese el mensaje que quiere decodificar. Solo puede contener letra o espacios: ")
    while not esValido(mensaje2):
        print("El mensaje solo puede contener letras y espacios.")
        mensaje2 = input("Ingrese el mensaje: ")
    return mensaje2

def vigenereDec(mensaje, clave):
        letras_a_numeros = {
           'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
           'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
           'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }

        numeros_a_letras = {
           0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g',
           7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
           14: 'ñ', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
           21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
        }

        texto_descodificado = ""

        posicion_clave = 0 

        for letra in mensaje:

            if letra in letras_a_numeros:

                valor_mensaje = letras_a_numeros[letra]

                letra_clave_actual = clave[posicion_clave]
                valor_clave = letras_a_numeros[letra_clave_actual]

                resta = valor_mensaje - valor_clave

                nuevo_valor = resta % 27

                nueva_letra = numeros_a_letras[nuevo_valor]

                texto_descodificado = texto_descodificado + nueva_letra

                posicion_clave = posicion_clave + 1

                if posicion_clave == len(clave):
                    posicion_clave = 0

            else:
                texto_descodificado = texto_descodificado + letra

        return texto_descodificado
    
ALFABETO = "abcdefghijklmnñopqrstuvwxyz"


def limpiarTexto(texto):
    texto = texto.lower()

    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }

    texto_limpio = ""

    for letra in texto:
        if letra in reemplazos:
            letra = reemplazos[letra]

        if letra in ALFABETO or letra == " ":
            texto_limpio += letra

    return texto_limpio

def cesarCod(texto, desplazamiento):
    if type(desplazamiento) != int:
        raise Exception("El desplazamiento debe ser un número entero")

    texto = limpiarTexto(texto)

    resultado = ""

    for caracter in texto:

        if caracter == " ":
            resultado += " "
        else:
            posicion = ALFABETO.index(caracter)

            nueva_posicion = (posicion + desplazamiento) % len(ALFABETO)

            resultado += ALFABETO[nueva_posicion]

    return resultado


def cesarDec(texto, desplazamiento):
    if type(desplazamiento) != int:
        raise Exception("El desplazamiento debe ser un número entero")

    texto = limpiarTexto(texto)

    resultado = ""

    for caracter in texto:

        if caracter == " ":
            resultado += " "
        else:
            posicion = ALFABETO.index(caracter)

            nueva_posicion = (posicion - desplazamiento) % len(ALFABETO)

            resultado += ALFABETO[nueva_posicion]

    return resultado
def railfenceCod(texto):
    mensaje = puntuación(texto)
    if type(mensaje) != list:
        raise Exception("El texto debe ser una lista")
    resultado = []
    línea1 = mensaje[0:len(mensaje):4]
    resultado.append(línea1)
    línea2 = mensaje[1:len(mensaje):2]
    resultado.append(línea2)
    línea3 = mensaje[2:len(mensaje):4]
    resultado.append(línea3)
    encriptado = "".join("".join(bloque) for bloque in resultado)
    return encriptado
def puntuación(texto):
    if type(texto) != str or texto == "":
        raise Exception("El texto debe ser de tipo string, y tener algo escrito dentro")
    texto = texto.replace(" ","-")
    lista1 = list(texto)
    símbolos = ".,:;¡!¿?#$%&/()=+*{[]}_"
    mensaje = []
    for letra in lista1:
        if letra not in símbolos:
            mensaje.append(letra)
    while len(mensaje)%4 != 0:
        mensaje.append("-")
    return mensaje
def limpiar_pantalla():
    """Función que se encarga de imprimir líneas en blanco para 'limpiar' la pantalla
No tiene entradas ni restricciones, solo imprime 40 líneas en blanco"""
    print("\n" * 10)
def repetir():
    """Función booleana que se encarga de preguntarle al usuario sí desea volver a utilizar el programa o no, además, en el caso de que la respuesta sea
negativa, se encarga de imprimir el mensaje de despedida.
Entradas: No tiene.
Restricciones: El usuario solo puede escribir 's' o 'n', además de que la salida es un valor booleano.
Salidas: True en el caso de que el usuario desee continuar, en caso contrario False, después de mostrar el mensaje de  despedida."""
    print()
    print("¿Desea volver a utilizar el programa?")
    respuesta=input("Digite 'S' en caso de que desea utilizarlo de nuevo, de lo contrario digite 'N': ")
    respuesta = respuesta.lower()
    while respuesta not in ["s","n"]:
        respuesta = input("¿Desea utiliza el programa de nuevo? Digite 'S' o 'N': ")
        respuesta = respuesta.lower()
    if respuesta == "s":
        return True
    else:
        print("Le agradecemos por utilizar el programa. Hasta luego")
        return False
main()
   
    
    
