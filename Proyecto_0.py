def main():
    #Falta el mensaje de bienvenida y la descripción.
    print("Por favor escoga alguno de los siguientes números, \
dependiendo del método de cifrado que desea utilizar")
    continuar = True
    while continuar:
        try:
             indicación=int(input("Diguite '1' para el método de cifrado césar; '2' para\
el cifrado monoalfabético con palabra clave; '3' para el cifrado vigenère; '4' para el \
el cifrado PlayFair; '5' para el cifrado Rail Fence; '6' para el cifrado escítala:  "))
             while indicación not in (1, 2, 3, 4, 5, 6):
                 indicación = int(input("Digite algún número válido para continuar: ")) #indicación es solo para seleccionar método
        #Acá se podría limpiar la pantalla. 
             if indicación == 1:
                 print("Cifrado César")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría cesarCod(texto, desplazamiento)
                 else:
                     print("Decodificar") # Acá iría cesarDec(texto, desplazamiento)
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
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría vigenereCod(texto, palabra)
                 else:
                     print("Decodificar") # Acá iría vigenerDec(texto, palabra)
             elif indicación == 4:
                 print("Cifrado PlayFair")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría playfairCod(texto, palabra)
                 else:
                     print("Decodificar") # Acá iría playfairDec(texto, palabra)
             elif indicación == 5:
                 print("Cifrado Rail Fence")
                 selección = int(input("Digite '1' si lo que desea es codificar, de lo contrario, digite '2' para decodificar: "))
                 while selección not in (1, 2):
                     selección=int(input("Digite uno de los valores válidos: "))
                 if selección == 1:
                     print("Codificar") # Acá iría railfenceCod(texto)
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
main()
   
    
    
