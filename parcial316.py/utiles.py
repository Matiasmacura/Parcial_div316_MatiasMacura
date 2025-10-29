
#Creo una matriz vacia 


def crear_matriz () -> list:
    """Funcion encargada de crear una matriz vacia.

    argumento : no se le pasan agrumentos para crear desde 0.

    retorna : retorna una matriz con la cantidad de filas y columnas selecionada dentro"""
    matriz= []
    vehiculos = int(input("Cuantos vehiculos desea ingresar al sistema: "))
    for i in range (vehiculos):
        fila = [0] * 5
        matriz += [fila]

    return matriz


#Cargamos los datos a la matriz:

def cargar_matriz (matriz : list) -> list:
    """" La funcion realiza una carga secuencial de una matriz.

    argumentos: Recine como parametro una matriz.

    retorna: la misma matriz pero ya cargada con los elementos deseados.
    """
    for i in range (len(matriz)):

        patente = input("Ingrese la patente del vehiculo: ")
        marca = input("Ingrese la marce del vehiculo: ")
        modelo = input ("Ingrese el modelo del mismo: ")
        año = int(input("Ingrese el año del vehiculo: "))
        horas_de_estacionamiento = int(input("Ingrese la cantidad de horas que estuvo estacionado: "))

        matriz [i][0] = patente
        matriz [i][1] = marca
        matriz [i][2] = modelo
        matriz [i][2] = año
        matriz [i][3] = horas_de_estacionamiento

    return matriz




#Mostramos la matriz como deberia verse 

def mostrar_matriz (matriz : list):
    """ Funcion encargada de mostrar la matriz en el formato deseado.

    argumento : Recibe como parametro una matriz.

    retorno : No retorna nada , solo muestra la misma matriz de la forma deseada.

     """
    for i in range (len(matriz)):
        print [matriz[i], "end=\n"]



#Buscamos el auto por patente


def buscar_por_patente (matriz:list) -> list:
    """ Funcion encargada de buscar por patente un auto en especifico.

    argumento : Recibe como parametro un matriz.

    retorno : Retorna solo el indicie deseado, el correspondiente a la patente encontrada (una lista).

    """


    patente_a_encontrar = input("Ingrese la patente que desea buscar: ")
    for i in range (len(matriz)):
        if patente_a_encontrar == matriz [i][0]:
            patente_a_encontrar = matriz [i]
            return patente_a_encontrar
            break
        else: 
            print ("No hay autos cargados al sistema con esa pantente: ")


#Ordenamos vehiculos por año

def ordenar_por_año_desendiente (matriz : list) -> list:
    """ Funcion encargada de ordenar los vehiculos de forma decendiente segun su año.

    argumento : Recibe como parametro un matriz.

    retorno : Retorna la misma matriz ordenada corresctamente.

    """

    n = len(matriz)
    matriz_ordenada = matriz [:]
    bandera = True


    while bandera == True:
        bandera = False
        for i in range (n-1):
            for j in range (n-1-i):
                if matriz_ordenada [i][3]  > matriz_ordenada [i+1][3]:
                    auxiliar = matriz_ordenada [i]
                    matriz_ordenada [i] = matriz_ordenada [i+1]
                    matriz_ordenada [i+1] = auxiliar
                    bandera = True
        
        return matriz_ordenada
    


#buscamos el vehiculo con mas horas estacionado.

def calcular_mas_horas_estacionados (matriz : list) -> list :
    """ Funcion encargada de calcular cual es el auto que mas tiempo lleva estacionado.

    argumento : Recibe como parametro un matriz.

    retorno :Retorna solo el indicie deseado, el correspondiente a la patente encontrada (una lista).

    """

    mas_horas_estacionado = float("-inf")
    
    for i in range (len(matriz)):
        if matriz [i][4] > mas_horas_estacionado:
            mas_horas_estacionado = matriz[i][4]
            datos_mas_horas_estacionado = matriz [i]
    return datos_mas_horas_estacionado

    
#buscamos el vehiculo con menos horas estacionado.


def calcular_menos_horas_estacionados (matriz : list) -> list:

    """ Funcion encargada de calcular cual es el auto que menos tiempo lleva estacionado.

    argumento : Recibe como parametro un matriz.

    retorno :Retorna solo el indicie deseado, el correspondiente a la patente encontrada (una lista).

    """

    menos_horas_estacionado = float("inf")
    
    for i in range (len(matriz)):
        if matriz [i][4] < menos_horas_estacionado:
            menos_horas_estacionado = matriz[i][4]
            datos_menos_horas_estacionado = matriz [i]
    return datos_menos_horas_estacionado

# buscamos los vehiculos con mas de 4 horas de estacionamiento 

def calcular_mas_de_cuatro_horas_estacionado (matriz):
    """ Funcion encargada de calcular cuantos autos llevan mas de 4 horas estacionados.

    argumento : Recibe como parametro un matriz.

    retorno :Retorna una matriz con todos los indices correspondientes a autos que superen las 4 hs de estacionamiento.

    """
    vehiculos_4_horas = []

    for i in range (len(matriz)):
        if matriz [i][4] > 4:
            vehiculos_4_horas += [matriz [i]]
        
    return vehiculos_4_horas

#calculamos el promedio de horas de los autos estacionados

def calcular_promedio_horas (matriz : list) -> float:

    """ Funcion encargada de calcular el promedio de horas de todos los autos estacionados.

    argumento : Recibe como parametro un matriz.

    retorno :Rerotna el promedio de horas de que llevan estacionados todos los autos. (un float)

    """
    acumulador_horas = 0

    for i in range (len(matriz)):
        acumulador_horas += matriz[i][4]
    
    promedio_de_horas = acumulador_horas / len(matriz)

    return promedio_de_horas

#buscamos la cantidad vehiculos de marca ford

def contar_vehiculos_ford (matriz : list) -> int:

    """ Funcion encargada de calcular cuantos autos de marca ford hay.

    argumento : Recibe como parametro un matriz.

    retorno :Retorna solo la cantidad de autos que cumplen dicho pedido. (un int)

    """
    contador_ford = 0

    for i in range (len(matriz)):
        if matriz [i][1] == "ford":
            contador_ford += 1
    
    return contador_ford




