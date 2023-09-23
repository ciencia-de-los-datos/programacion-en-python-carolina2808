"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    suma_segunda_columna = 0
    with open("data.csv","r") as data:
        for linea in data:
            
            col = linea.strip().split('\t')
            if len(col) >= 2:
            
                valor_segunda_columna = int(col[1])
                suma_segunda_columna += valor_segunda_columna
 

    return suma_segunda_columna


def pregunta_02():
    recuento_letras = {}
    with open("data.csv","r") as data:
        for linea in data:
            # Dividir la línea en columnas utilizando el separador de tabulación ("\t")
            col = linea.strip().split('\t')
            
            # Verificar si hay al menos una columna en la línea
            if len(col) >= 1:
                # Obtener la primera letra de la primera columna
                primera_letra = col[0][0].upper()  # Convertir a mayúscula
                
                # Actualizar el recuento de la letra en el diccionario
                if primera_letra in recuento_letras:
                    recuento_letras[primera_letra] += 1
                else:
                    recuento_letras[primera_letra] = 1

        lista_tuplas = sorted(recuento_letras.items())
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return lista_tuplas


def pregunta_03():
    suma_por_letra = {}
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 2:
                letra_columna1 = columnas[0]
                valor_columna2 = int(columnas[1])
                

                if letra_columna1 in suma_por_letra:
                    suma_por_letra[letra_columna1] += valor_columna2
                else:
                    suma_por_letra[letra_columna1] = valor_columna2


        lista_tuplas = list(suma_por_letra.items())


        lista_tuplas.sort(key=lambda x: x[0])
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return lista_tuplas


def pregunta_04():
 
    recuento_por_mes = {}
    with open("data.csv","r") as data:
        for linea in data:
            col = linea.strip().split('\t')
            
            if len(col) >= 3:
                fecha = col[2]
                dividirfecha = fecha.split('-')
                if len(dividirfecha) == 3:
                    mes = dividirfecha[1]
                    if mes in recuento_por_mes:
                        recuento_por_mes[mes] += 1
                    else:
                        recuento_por_mes[mes] = 1

    # Crear una lista de tuplas a partir del diccionario y ordenarla por mes
        lista_tuplas = sorted(recuento_por_mes.items())
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return lista_tuplas


def pregunta_05():
    max_min_por_letra = {}
    with open("data.csv","r") as data:
        for linea in data:
            
            col = linea.strip().split('\t')
            
            if len(col) >= 2:
                letra = col[0]
                valor_col2 = int(col[1])
                
                if letra in max_min_por_letra:
                    max_valor, min_valor = max_min_por_letra[letra]
                    max_valor = max(max_valor, valor_col2)
                    min_valor = min(min_valor, valor_col2)
                    max_min_por_letra[letra] = (max_valor, min_valor)
                else:
                    max_min_por_letra[letra] = (valor_col2, valor_col2)

        lista_tuplas = [(letra, max_valor, min_valor) for letra, (max_valor, min_valor) in max_min_por_letra.items()]

        lista_tuplas.sort(key=lambda x: x[0])

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return lista_tuplas


def pregunta_06():
    valores_minimos_maximos = {}
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')
            
            if len(columnas) >= 5:
                valores_columna5 = columnas[4].split(',')  

                for valor in valores_columna5:
                    clave, valor_asociado = valor.split(':')
                    clave = clave.strip()
                    valor_asociado = int(valor_asociado)
                    
                    if clave in valores_minimos_maximos:
                        min_valor, max_valor = valores_minimos_maximos[clave]
                        min_valor = min(min_valor, valor_asociado)
                        max_valor = max(max_valor, valor_asociado)
                        valores_minimos_maximos[clave] = (min_valor, max_valor)
                    else:
                        valores_minimos_maximos[clave] = (valor_asociado, valor_asociado)

        lista_tuplas = [(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in valores_minimos_maximos.items()]

        lista_tuplas.sort(key=lambda x: x[0])
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return lista_tuplas


def pregunta_07():
    asociaciones = {}
    with open("data.csv","r") as data:
        for linea in data:
            col = linea.strip().split('\t')
            
            if len(col) >= 3:
                valor_col2 = int(col[1])
                letra_col1 = col[0]
                
                if valor_col2 in asociaciones:
                    asociaciones[valor_col2].append(letra_col1)
                else:
                    asociaciones[valor_col2] = [letra_col1]

        lista_tuplas = [(valor, letras) for valor, letras in asociaciones.items()]

        lista_tuplas.sort(key=lambda x: x[0])
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return lista_tuplas


def pregunta_08():

    asociaciones = {}
    with open("data.csv","r") as data:
        for linea in data:

            columnas = linea.strip().split('\t')
            if len(columnas) >= 3:
                valor_columna2 = int(columnas[1])
                letra_columna1 = columnas[0]

                if valor_columna2 in asociaciones:
                    if letra_columna1 not in asociaciones[valor_columna2]:
                        asociaciones[valor_columna2].append(letra_columna1)
                else:
                    asociaciones[valor_columna2] = [letra_columna1]

        lista_tuplas = [(valor, sorted(letras)) for valor, letras in asociaciones.items()]

        lista_tuplas.sort(key=lambda x: x[0])
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return lista_tuplas


def pregunta_09():
    recuento_claves_columna5 = {}
    with open("data.csv","r") as data:
        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 5:
                claves = columnas[4].split(',')
                
                for clave in claves:
                    clave = clave.split(':')[0]  
                    clave = clave.strip()  
                    
                    if clave in recuento_claves_columna5:
                        recuento_claves_columna5[clave] += 1
                    else:
                        recuento_claves_columna5[clave] = 1
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return recuento_claves_columna5


def pregunta_10():
    lista_tuplas = []
    with open("data.csv","r") as data:

        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 5:
                letra_columna1 = columnas[0]

                elementos_columna4 = columnas[3].split(',')
                elementos_columna5 = columnas[4].split(',')
                lista_tuplas.append((letra_columna1, len(elementos_columna4), len(elementos_columna5)))
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return lista_tuplas


def pregunta_11():

    suma_por_letra = {}
    with open("data.csv","r") as data:
        for linea in data:
            columnas = linea.strip().split('\t')

            if len(columnas) >= 4:
                letras_columna4 = columnas[3].split(',')  
                valor_columna2 = int(columnas[1])
                
                for letra in letras_columna4:
                    letra = letra.strip()  
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor_columna2
                    else:
                        suma_por_letra[letra] = valor_columna2


        suma_por_letra_ordenada = dict(sorted(suma_por_letra.items()))
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return suma_por_letra_ordenada


def pregunta_12():
    suma_por_letra_columna1 = {}
    with open("data.csv","r") as data:

    
        for linea in data:
            
            columnas = linea.strip().split('\t')
            
            if len(columnas) >= 5:
                letra_columna1 = columnas[0]
                valores_columna5 = columnas[4].split(',') 
                
                suma = sum(int(valor.split(':')[1]) for valor in valores_columna5)
                
                if letra_columna1 in suma_por_letra_columna1:
                    suma_por_letra_columna1[letra_columna1] += suma
                else:
                    suma_por_letra_columna1[letra_columna1] = suma
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return suma_por_letra_columna1
