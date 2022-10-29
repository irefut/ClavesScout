    # -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:02:50 2022

@author: Irene

Cifrado de claves:
    
    Están:
        Clave murciélago           * string = claveMurcielago(texto) *
        Clave Abecedario o inversa * string = claveABC(texto) *
        Clave Malespín (Pita mobe) * string = claveMalespin(texto) *
        Clave Numérica             * string = claveNumerica(texto) *
        
    Las entradas NO deben contener ninguna palabra tildada y deben estar 
    solamente en mayúscula.
    
    Además de los caracteres regulares de letras están inccluidos 
    -el espacio ' '
    -las comillas '"'
    -el punto '.'
    -la coma ','
    -signos de interrogación '¿' y '?'
    -guión '-'
    
    Cualquier otro caracter no verá ningún cambio y se escribirá tal y 
    como viene.
    
"""
def claveABC(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print("msj entrada para abecedario/inversa: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "A":
            mensajecifrado = mensajecifrado + "Z"        
        elif texto[i] == "B":
            mensajecifrado = mensajecifrado + "Y"
        elif texto[i] == "C":
            mensajecifrado = mensajecifrado + "X"
        elif texto[i] == "D":
            mensajecifrado = mensajecifrado + "W"
        elif texto[i] == "E":
            mensajecifrado = mensajecifrado + "V"
        elif texto[i] == "F":
            mensajecifrado = mensajecifrado + "U"
        elif texto[i] == "G":
            mensajecifrado = mensajecifrado + "T"
        elif texto[i] == "H":
            mensajecifrado = mensajecifrado + "S"
        elif texto[i] == "I":
            mensajecifrado = mensajecifrado + "R"
        elif texto[i] == "J":
            mensajecifrado = mensajecifrado + "Q"
        elif texto[i] == "K":
            mensajecifrado = mensajecifrado + "P"
        elif texto[i] == "L":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "M":
            mensajecifrado = mensajecifrado + "Ñ"
        elif texto[i] == "N":
            mensajecifrado = mensajecifrado + "N"
        elif texto[i] == "Ñ":
            mensajecifrado = mensajecifrado + "M"
        elif texto[i] == "O":
            mensajecifrado = mensajecifrado + "L"
        elif texto[i] == "P":
            mensajecifrado = mensajecifrado + "K"
        elif texto[i] == "Q":
            mensajecifrado = mensajecifrado + "J"
        elif texto[i] == "R":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "S":
            mensajecifrado = mensajecifrado + "H"
        elif texto[i] == "T":
            mensajecifrado = mensajecifrado + "G"
        elif texto[i] == "U":
            mensajecifrado = mensajecifrado + "F"
        elif texto[i] == "V":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "W":
            mensajecifrado = mensajecifrado + "D"
        elif texto[i] == "X":
            mensajecifrado = mensajecifrado + "C"
        elif texto[i] == "Y":
            mensajecifrado = mensajecifrado + "B"
        elif texto[i] == "Z":
            mensajecifrado = mensajecifrado + "A"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('\n')
    print('msj salida para abecedario: '+mensajecifrado)
    return mensajecifrado

def claveMalespin(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print("msj entrada para malespin: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "P":
            mensajecifrado = mensajecifrado + "M"        
        elif texto[i] == "I":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "T":
            mensajecifrado = mensajecifrado + "B"
        elif texto[i] == "A":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "M":
            mensajecifrado = mensajecifrado + "P"
        elif texto[i] == "O":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "B":
            mensajecifrado = mensajecifrado + "T"
        elif texto[i] == "E":
            mensajecifrado = mensajecifrado + "A"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('\n')
    print('msj salida para malespín: '+mensajecifrado)
    return mensajecifrado

def claveMurcielago(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print("msj entrada para murciélago: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "M":
            mensajecifrado = mensajecifrado + "0"        
        elif texto[i] == "U":
            mensajecifrado = mensajecifrado + "1"
        elif texto[i] == "R":
            mensajecifrado = mensajecifrado + "2"
        elif texto[i] == "C":
            mensajecifrado = mensajecifrado + "3"
        elif texto[i] == "I":
            mensajecifrado = mensajecifrado + "4"
        elif texto[i] == "E":
            mensajecifrado = mensajecifrado + "5"
        elif texto[i] == "L":
            mensajecifrado = mensajecifrado + "6"
        elif texto[i] == "A":
            mensajecifrado = mensajecifrado + "7"
        elif texto[i] == "G":
            mensajecifrado = mensajecifrado + "8"
        elif texto[i] == "O":
            mensajecifrado = mensajecifrado + "9"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('\n')
    print('msj salida para murciélago: '+mensajecifrado)
    return mensajecifrado

def claveNumerica(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print("msj entrada para numérica: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + "/"
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "--"
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "//"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?//"
        elif texto[i] == "A":
            mensajecifrado = mensajecifrado + "1."        
        elif texto[i] == "B":
            mensajecifrado = mensajecifrado + "2."
        elif texto[i] == "C":
            mensajecifrado = mensajecifrado + "3."
        elif texto[i] == "D":
            mensajecifrado = mensajecifrado + "4."
        elif texto[i] == "E":
            mensajecifrado = mensajecifrado + "5."
        elif texto[i] == "F":
            mensajecifrado = mensajecifrado + "6."
        elif texto[i] == "G":
            mensajecifrado = mensajecifrado + "7."
        elif texto[i] == "H":
            mensajecifrado = mensajecifrado + "8."
        elif texto[i] == "I":
            mensajecifrado = mensajecifrado + "9."
        elif texto[i] == "J":
            mensajecifrado = mensajecifrado + "10."
        elif texto[i] == "K":
            mensajecifrado = mensajecifrado + "11."
        elif texto[i] == "L":
            mensajecifrado = mensajecifrado + "12."
        elif texto[i] == "M":
            mensajecifrado = mensajecifrado + "13."
        elif texto[i] == "N":
            mensajecifrado = mensajecifrado + "14."
        elif texto[i] == "Ñ":
            mensajecifrado = mensajecifrado + "15."
        elif texto[i] == "O":
            mensajecifrado = mensajecifrado + "16."
        elif texto[i] == "P":
            mensajecifrado = mensajecifrado + "17."
        elif texto[i] == "Q":
            mensajecifrado = mensajecifrado + "18."
        elif texto[i] == "R":
            mensajecifrado = mensajecifrado + "19."
        elif texto[i] == "S":
            mensajecifrado = mensajecifrado + "20."
        elif texto[i] == "T":
            mensajecifrado = mensajecifrado + "21."
        elif texto[i] == "U":
            mensajecifrado = mensajecifrado + "22."
        elif texto[i] == "V":
            mensajecifrado = mensajecifrado + "23."
        elif texto[i] == "W":
            mensajecifrado = mensajecifrado + "24."
        elif texto[i] == "X":
            mensajecifrado = mensajecifrado + "25."
        elif texto[i] == "Y":
            mensajecifrado = mensajecifrado + "26."
        elif texto[i] == "Z":
            mensajecifrado = mensajecifrado + "27."
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('\n')
    print('msj salida para numérica: '+mensajecifrado)
    return mensajecifrado

#a = claveABC("PREGUNTATE SI LO QUE ESTAS HACIENDO HOY TE ACERCA AL LUGAR EN EL QUE QUIERES ESTAR MAÑANA.")
#print("eso es a: "+a)
#b = claveMalespin("CUELQUOAR CISE ASBI AS PELASMON")
#print("esto es b: "+b)
#c = claveNumerica('"ABCDEF GHIJKL.MNÑO, PQRST\ "MENSAJE" -UVW XYZ')
#e = claveMurcielago('HOLA SOY IRENE ESTO ES CLAVE MURCIELAGO')
#print('esto es e: ' + e)

msj1 = '“PREGUNTATE SI LO QUE ESTAS HACIENDO HOY TE ACERCA AL LUGAR EN EL QUE QUIERES ESTAR MAÑANA.” -WALT DISNEY'
msj2 = '“SERVICIO ES HACER A UN LADO EL PLACER O LA CONVENIENCIA PARA TENDER LA MANO AL NECESITADO.” -BADEN POWELL'
msj3 = '“LA MEJOR VIDA NO ES LA MAS DURADERA, SINO MAS BIEN AQUELLA QUE ESTA REPLETA DE BUENAS ACCIONES.” -MARIE CURIE'
msj4 = '“¿DE QUE SIRVE GANAR MIL BATALLAS SI NO PUEDES VENCER TUS PROPIAS PASIONES? LA VERDADERA BATALLA TIENE LUGAR DENTRO DE NOSOTROS MISMOS.” -CARLO ACUTIS'
msj5 = '"QUIERO SER LA MEJOR VERSION DE MI MISMA." -HANNA GABRIELS'
msj6 = '“… LA VIDA NO LLEGA A UNO CON UN SENTIDO, SINO QUE EN SU TRANSCURRIR LE OTORGA A LA PERSONA UNA SERIE DE POTENCIAS, DE RECURSOS, PARA QUE UNO SEA QUIEN LE DE UN SENTIDO.” -LILIA RAMOS'

msjCod1 = claveMalespin(msj5)
msjCod2 = claveNumerica(msjCod1)

#print(msjCod1)