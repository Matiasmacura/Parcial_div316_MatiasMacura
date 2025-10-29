from utiles import crear_matriz, cargar_matriz, calcular_mas_de_cuatro_horas_estacionado, calcular_mas_horas_estacionados, calcular_promedio_horas, calcular_menos_horas_estacionados, contar_vehiculos_ford, mostrar_matriz, buscar_por_patente, ordenar_por_año

matriz_vehiculos = []
menu = ("Bienvenido a Parkin Center!! \n 1_Cargar vehiculos al sistema. \n 2_Mostrar la lista de vehiculos ya cargados.\n 3_Buscar vehiculo por pantente. \n 4_Ordenar vehiculos por año de manera descendente \n 5_Mostrar vehiculo con mas horas estacionado \n 6_Mostrar vehiculos con menos horas estacionado \n 7_Mostrar cantidad de vehiculos con mas de 4 horas estacionado. \n 8_Mostrar el promedio de horas estacionadas de todos los vehiculos. \n 9_Mostar cantidad de vehiculos de marca ford \n 10_salir." )

seguir = "si"

while seguir :
    print (menu)
    opcion_ingresada = int(input("Por favor, ingrese la opcion deseada: "))
    if opcion_ingresada == 1 or opcion_ingresada == 10 or len(matriz_vehiculos) > 0:
        match opcion_ingresada:
            case 1: #Cargamos los vehiculos
                matriz_vehiculos = crear_matriz()
                cargar_matriz(matriz_vehiculos)
            case 2:#Mostramos los autos ya cargados al sistema
                (f"Los autos ya cargados al sistema son {mostrar_matriz(matriz_vehiculos)}") 
            case 3:#Buscamos un vehiculo por su patente
                (f"La patante ingresada corresponde al auto {buscar_por_patente(matriz_vehiculos)}")
            case 4:#Ordenamos la matriz
                print (ordenar_por_año(matriz_vehiculos))
            case 5:#Mostramos el vehiculo con mas horas estacionado.
                (f"El vehiculo que mas horas tiene estacionado{calcular_mas_horas_estacionados(matriz_vehiculos)}")
            case 6:#Mostramos el vehiculo con menos horas estacionado.
                (f"El vehiculo que menos horas tiene estacionado{calcular_menos_horas_estacionados(matriz_vehiculos)}")
            case 7:#Mostramos los vehiculos con mas de 4 horas estacionados.
                (f"Los vehiculos que llevan mas de 4 horas estacionados son {calcular_mas_de_cuatro_horas_estacionado(matriz_vehiculos)}")
            case 8:#Calculamos el promedio de horas.
                (f"El promedio de horas estacionados de todos los autos en el parkin es {calcular_promedio_horas(matriz_vehiculos)}")
            case 9:#Contamos vehiculos ford.
                (f"La cantidad de vehiculos de marca ford en el parkin es de {contar_vehiculos_ford}")
            case 10:#Salir.
                print("Hasta pronto!...")
                seguir = "no"
    else: 
        print("No hay vehiculos cargados para la opcion solicitada.")
    input("\nPresioná Enter para volver al menu...")
