# Primero llamamos todos los archivos al archivo principal en este caso la interfaz
import registro_equipo2
import registro_plantel2
import programar_partidos2
import registrar_resultados2
import mostrar_resultados2

# Creamos equipos y partidos
equipos = []
partidos = []

# Iniciamos el while
while True:
    print("""
    ----------------------------
       L.I.G.A  B.E.T.P.L.A.Y
    ----------------------------
    """)
    # Mostramos la interfaz 
    print("Menu:")
    # Mostramos las posibles opciones
    print("  1. Registrar Equipos")
    print("  2. Registro Plantel")
    print("  3. Programar partido")
    print("  4. Registrar resultado")
    print("  5. Ver equipos")
    print("  6. Salir")
    # Le pedimos al usuario que ingrese su opción
    opcion = input("Ingresa una opcion -> ")

    # Si se cumple, nos manda a los archivos con cada nombre
    if opcion == "1":
        registro_equipo2.crear_equipo(equipos)
    elif opcion == "2":
        registro_plantel2.registro_plantel(equipos)
    elif opcion == "3": 
        programar_partidos2.programar_partidos(equipos, partidos)
    elif opcion == "4":
        registrar_resultados2.registrar_resultados(partidos, equipos)
    elif opcion == "5":
        mostrar_resultados2.mostrar_equipos(equipos)  
    elif opcion == "6":
        break
    else: 
        print("Ingresaste una respuesta INCORRECTA, Intenta de nuevo")
        input("Presiona ENTER para continuar -> ")    


