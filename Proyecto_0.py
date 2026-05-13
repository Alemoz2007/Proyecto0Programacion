def main():
    bienvenida()
    print()
    print("Por favor escoga alguno de los siguientes números, \
dependiendo del método de cifrado que desea utilizar")
    continuar = True
    while continuar:
        try:
             print()
             indicación=input("Digite '1' para el método de cifrado césar; '2' para \
el cifrado monoalfabético con palabra clave; '3' para el cifrado vigenère; '4' para el \
el cifrado PlayFair; '5' para el cifrado Rail Fence; '6' para el cifrado escítala:  ")
             limpiar_pantalla()
             while indicación not in ["1","2","3","4","5","6"]:
                 print("Indicación invalida") 
                 indicación = input("Digite algún número válido para continuar: ")
                 limpiar_pantalla()
             if indicación == "1":
                 print("Cifrado César")
                 selección = input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: ")
                 while selección not in ("1", "2"):
                     selección=input("Digite uno de los valores válidos: ")

                 texto = input("Digite el texto: ")
                 while not esValido(texto):
                     print("El mensaje solo puede contener letras y espacios.")
                     texto = input("Ingrese el mensaje: ")
                 texto = texto

                 desplazamiento = int(input("Digite el desplazamiento: "))

                 if selección == "1":
                  resultado = cesarCod(texto, desplazamiento)
                  print("Texto codificado:")
                  print(resultado)
                 else:
                   resultado = cesarDec(texto, desplazamiento)
                   print("Texto decodificado:")
                   print(resultado)
             elif indicación == "2":
                 print("Cifrado Monoalfabético con Palabra Clave")
                 selección = input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: ")
                 while selección not in ("1", "2"):
                     selección=input("Digite uno de los valores válidos: ")
                 texto = input("Digite el texto: ")
                 while not esValido(texto):
                     print("El mensaje solo puede contener letras y espacios.")
                     texto = input("Ingrese el mensaje: ")
                 texto = texto
                 palabra = input( "Digite la palabra clave: " )

                 if selección == "1":
                    resultado = monoCod(texto,palabra)
                    print("Texto codificado:")
                    print(resultado)
                 else:
                    resultado = monoDec(texto,palabra)
                    print("Texto decodificado:")
                    print(resultado)
             elif indicación == "3":
                 print("Cifrado Vigenère")
                 mainVigenere()
                 print()
             elif indicación == "4":
                 print("Cifrado PlayFair")
                 mainPlayfair()
                 print()
             elif indicación == "5":
                 print("Cifrado Rail Fence")
                 selección = input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: ")
                 while selección not in ("1", "2"):
                     selección=input("Digite uno de los valores válidos: ")
                 if selección == "1":
                     texto=input("Diguite el texto que desea codificar: ")
                     print (f"Su texto codificado es: {railfenceCod(texto)}")
                 else:
                     texto=input("Diguite el texto que desea descodificar: ")
                     if type(texto) != str or texto == "":
                         raise Exception("El texto debe ser de tipo string, y tener algo escrito dentro")
                     print (f"Su texto descodificado es: {railfenceDec(texto)}")
             else:
                 print("Cifrado Escítala")
                 selección = input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: ")
                 while selección not in ("1", "2"):
                     selección=input("Digite uno de los valores válidos: ")
                 if selección == "1":
                     texto=input("Diguite el texto que desea codificar: ")
                     lineas = int(input("Digite la cantidad de letras que desea en cada 'vuelta': "))
                     print (f"Su texto codificado es: {escitalaCod(texto, lineas)}")
                 else:
                     texto=input("Diguite el texto que desea descodificar: ")
                     lineas = int(input("Digite la cantidad de letras que hay en cada 'vuelta': "))
                     print (f"Su texto descodificado es: {escitalaDec(texto, lineas)}")
        except Exception as e:
            print(f"Error:{e}")
            continuar = False
        limpiar_pantalla()
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
        print("La palabra clave solo puede contener letras.")
        clave = input("Ingrese la palabra clave: ")
    return clave

def elegirOpcion():
    """Subrutina que se le pregunta al usuario si quiere codificar o decodificar su texto.
    Entradas y restricciones:
    -1 si el usuario quiere codificar, 2 si quiere decodificar (Las unicas respuestas que se aceptan son 1 o 2)
    Salidas: Inicia la funcion de codificacion si eligio 1, decodificacion si eligio 2."""
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

def mainPlayfair():
    """Programa principal del algoritmo playfair.
    Entradas y restricciones:
    -Palabra clave.
    -Texto a codificar o decodificar dependiendo de las preferencias del usuario.
    Salidas: Palabra codifica o decodificada."""
    clave = leerClave()
    texto_clave = preparar(clave)
    matriz = crearMatriz(texto_clave)
    opcion = elegirOpcion()
    if opcion == "1":
        mensaje = leerMensaje()
        texto_mensaje = preparar(mensaje)
        texto_codificado = playfairCod(texto_mensaje, texto_clave)
        print("Texto codificado:", texto_codificado)
    elif opcion == "2":
        mensaje2 = leerMensaje2()
        texto_mensaje2 = preparar(mensaje2)
        texto_decodificado = playfairDec(texto_mensaje2, texto_clave)
        print("Texto decodificado:", texto_decodificado)


def crearMatriz(clave):
    """Funcion que se encarga de crear la matriz para codificar o decodificar el texto, dependiendo de las preferencias del usuario.
    Entradas y restricciones:
    -Palabra clave.
    Salidas: La matriz."""
    alfabeto = "abcdefghijklmnñopqrstuvwxyz123"
    usadas = ""
    for letra in clave:
        if letra not in usadas and letra != " ":
            usadas += letra
    for letra in alfabeto:
        if letra not in usadas:
            usadas += letra
    matriz = []
    posicion = 0
    for fila in range(6):
        fila_actual = []
        for columna in range(5):
            if posicion < len(usadas):
                fila_actual.append(usadas[posicion])
                posicion += 1
        matriz.append(fila_actual)
    return matriz

def buscarLetra(matriz, letra):
    """Funcion que se encarga de encontrar la posicion de cada letra de la matriz.
    Entradas y restricciones:
    -Matriz
    Salidas: La posicion de cada letra dentro de la matriz."""
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == letra:
                return fila, columna

def separarPares(mensaje):
    """Funcion que se encarga de agregar un 1 si el texto tiene letras repetidas.
    Entradas y restricciones:
    -Texto a codificar o decodificar.
    Salidas: Texto pulido."""
    pares = []
    mensaje = mensaje.replace(" ", "")
    if len(mensaje) % 2 != 0:
        mensaje += "1"
    for i in range(0, len(mensaje), 2):
        pares.append(mensaje[i] + mensaje[i + 1])
    return pares

def ponerEspacios(texto_original, texto_nuevo):
    """Funcion que se encarga de agregar los espacios al texto original una vez codificado o decodificado.
    Entrada y restricciones:
    -Texto sin espacios
    Salidas: Texto con espacios."""
    resultado = ""
    posicion = 0
    for caracter in texto_original:
        if caracter == " ":
            resultado += " "
        else:
            resultado += texto_nuevo[posicion]
            posicion += 1
    while posicion < len(texto_nuevo):
        resultado += texto_nuevo[posicion]
        posicion += 1
    return resultado

def playfairCod(mensaje, clave):
    """Funcion para la codificacion de el algoritmo playfair.
    Entradas y restricciones:
    -Palabra clave
    -Texto a codificar
    Salidas: Texto codificado."""
    matriz = crearMatriz(clave)
    mensaje_original = mensaje
    mensaje = mensaje.replace(" ", "")
    pares = separarPares(mensaje)
    texto_codificado = ""
    for par in pares:
        letra1 = par[0]
        letra2 = par[1]
        fila1, col1 = buscarLetra(matriz, letra1)
        fila2, col2 = buscarLetra(matriz, letra2)
        if fila1 == fila2:
            nueva1 = matriz[fila1][(col1 + 1) % len(matriz[fila1])]
            nueva2 = matriz[fila2][(col2 + 1) % len(matriz[fila2])]
        elif col1 == col2:
            nueva1 = matriz[(fila1 + 1) % len(matriz)][col1]
            nueva2 = matriz[(fila2 + 1) % len(matriz)][col2]
        else:
            nueva1 = matriz[fila1][col2]
            nueva2 = matriz[fila2][col1]
        texto_codificado += nueva1 + nueva2
    texto_codificado = ponerEspacios(mensaje_original, texto_codificado)
    return texto_codificado

def playfairDec(mensaje, clave):
    """Funcion que se encarga de la decodificacion del algoritmo playfair.
    Entradas y restricciones:
    -Palabra clave
    -Texto a decodificar
    Salidas: Texto decodificado."""
    matriz = crearMatriz(clave)
    mensaje_original = mensaje
    mensaje = mensaje.replace(" ", "")
    pares = separarPares(mensaje)
    texto_decodificado = ""
    for par in pares:
        letra1 = par[0]
        letra2 = par[1]
        fila1, col1 = buscarLetra(matriz, letra1)
        fila2, col2 = buscarLetra(matriz, letra2)
        if fila1 == fila2:
            nueva1 = matriz[fila1][(col1 - 1) % len(matriz[fila1])]
            nueva2 = matriz[fila2][(col2 - 1) % len(matriz[fila2])]
        elif col1 == col2:
            nueva1 = matriz[(fila1 - 1) % len(matriz)][col1]
            nueva2 = matriz[(fila2 - 1) % len(matriz)][col2]
        else:
            nueva1 = matriz[fila1][col2]
            nueva2 = matriz[fila2][col1]
        texto_decodificado += nueva1 + nueva2
    texto_decodificado = ponerEspacios(mensaje_original, texto_decodificado)
    if texto_decodificado[-1] == "1":
        texto_decodificado = texto_decodificado[:-1]
    return texto_decodificado

    
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
    """Función "principal" de la codificación del cifrado rail fence.
Entradas: un string, la frase a codificar.
Restricciones: la frase debe ser de tipo string, al igual que la salida.
Salidas: Un string la frase codificada.
(Utiliza la función puntuación(texto)"""
    if not texto.strip() or texto.isdigit():
        raise Exception("El texto que ingresó es inválido, o contiene número o no ingresó nada")
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
    espacios = [encriptado[i:i+5] for i in range(0, len(encriptado), 5)]
    encriptado = " ".join(espacios)
    return encriptado
def puntuación(texto):
    """Se encarga de prepara la frase introducida en la función railfenceCod y escitalaCod, para facilitar su codificación.
Entradas: Un string, la frase a preparar.
Restriciones: La entrada debe ser un string, mientras que la salida una lista.
Salidas: Una lista que contiene la frase original, solo que en este formato, sin símbolos raros ni espacios, intercambia estos por guiones y se asegura que la salida sea multiplo de cuatro."""
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
def railfenceDec(texto):
     """Función "principal" de la descodificación del cifrado rail fence.
Entradas: un string, la frase a descodificar.
Restricciones: la frase debe ser de tipo string, además de que la longitud del texto debe ser múltiplo de cuatro(sin los espacios) al igual que la salida.
Salidas: Un string la frase descodificada.
(Utiliza la función combinar(línea1, línea2, línea3)"""
     if not texto.strip() or texto.isdigit():
        raise Exception("El texto que ingresó es inválido, o contiene número o no ingresó nada")
     texto = texto.replace(" ","")
     if type(texto) != str or len(texto)%4 != 0:
         raise Exception("El dato debe ser un string y debe ser múltiplo de 4")
     mensaje = list(texto)
     línea1 = mensaje[:len(texto)//4:]
     línea2 = mensaje[(len(texto)//4):(len(texto)//4) + len(texto)//2:]
     línea3 = mensaje[(len(texto)//4) + len(texto)//2:(len(texto)//4) + len(texto)//2 + len(texto)//4:]
     resultado = combinar(línea1, línea2, línea3)
     desencriptado = "".join("".join(bloque) for bloque in resultado)
     desencriptado = desencriptado.replace("-"," ")
     desencriptado = desencriptado.strip()
     return desencriptado
    
def combinar(línea1, línea2, línea3):
    """Se encarga de crear una única lista con las líneas del rail fence del railfenceDec, además de acomodarlas para que tengan sentido lógico.
Entradas: Las tres líneas del railfenceDec, estas deben ser listas y contener letras adentro.
Restricciones: Tanto las entradas como las salidas deben ser listas.
Salidas: Una lista con las letras de la frase a descodificar ordenadas."""
    if type(línea1) != list or type(línea2) != list or type(línea3) != list:
        raise Exception("Las listas no son listas")
    resultado = []
    while línea1 and línea2 and línea3:
        resultado.append(línea1.pop(0))
        resultado.append(línea2.pop(0))
        resultado.append(línea3.pop(0))
        resultado.append(línea2.pop(0))
    return resultado

def escitalaCod(texto, lineas):
    """Función que se encarga de codificar el texto del cifrado escítala
Entradas: Un texto a codificar (String) y el número de letras que cabe encada "vuelta" (int)
Restricciones: El texto debe ser de tipo str, al igual que la salida, mientras que el numero de lineas debe ser un entero mayor a 1
Salidas: Un string, el texto codificado
(Utiliza la función puntuación(texto)"""
    if not texto.strip() or texto.isdigit() or type(lineas) != int or lineas < 1:
        raise Exception("Alguno de los valores que ingresó es un valor inválido, por favor intente de nuevo")
    mensaje = puntuación(texto)
    while len(mensaje) % lineas != 0:
        mensaje.append("-")
    filas = [[]for _ in range(lineas)]
    for i, c in enumerate(mensaje):
        filas[i % lineas].append(c)
    codificado = "".join("".join(fila) for fila in filas)
    bloques = [codificado[i:i+5] for i in range(0, len(codificado), 5)]
    mensaje = " ".join(bloques)
    return mensaje

def escitalaDec(texto, lineas):
    """Función que se encarga de descodificar el texto del cifrado escítala
Entradas: Un texto a descodificar (String) y el número de letras que cabe encada "vuelta" (int)
Restricciones: El texto debe ser de tipo str, al igual que la salida, además de que la longitud de la entrada debe ser multiplo del número de líneas. Mientras que el numero de lineas debe ser un entero mayor a 1 
Salidas: Un string, el texto descodificado"""
    texto = texto.replace(" ","")
    if not texto.strip() or texto.isdigit() or len(texto)%lineas != 0 or type(lineas) != int or lineas < 1:
        raise Exception("Revisé los valores qué ingresó, alguno de ellos es inválido")
    columna = len(texto)//lineas
    filas = []
    i = 0
    for _ in range(lineas):
        filas.append(list(texto[i:i+columna]))
        i += columna
    mensaje = []
    for j in range(columna):
        for i in range(lineas):
            mensaje.append(filas[i][j])
    mensaje = "".join(mensaje).replace("-", " ")
    mensaje = mensaje.rstrip()
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

def crearAlfabetoClave(palabra):
    palabra = limpiarTexto(palabra)
    if palabra == "":
        raise Exception(
            "La palabra clave no puede estar vacía"
        )
    clave_sin_repetidas = ""
    for letra in palabra:
        if letra != " " and letra not in clave_sin_repetidas:
            clave_sin_repetidas += letra
    alfabeto_cifrado = clave_sin_repetidas
    for letra in ALFABETO:
        if letra not in alfabeto_cifrado:
            alfabeto_cifrado += letra
    return alfabeto_cifrado

def monoCod(texto, palabra):
    texto = limpiarTexto(texto)
    alfabeto_cifrado = crearAlfabetoClave(
        palabra
    )
    resultado = ""
    for caracter in texto:
        if caracter == " ":
            resultado += " "
        else:
            posicion = ALFABETO.index(caracter)
            resultado += alfabeto_cifrado[posicion]
    return resultado

def monoDec(texto, palabra):
    texto = limpiarTexto(texto)
    alfabeto_cifrado = crearAlfabetoClave(
        palabra
    )
    resultado = ""
    for caracter in texto:
        if caracter == " ":
            resultado += " "
        else:
            posicion = alfabeto_cifrado.index(
                caracter
            )
            resultado += ALFABETO[posicion]
    return resultado
main()
   
    
    
