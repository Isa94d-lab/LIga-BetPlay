def registrar_resultados(partidos, equipos):
    while True:  # Permitir que se registren varios resultados hasta que el usuario decida volver al menú
        print("""
    ------------------------------------
       REGISTRAR RESULTADO DE PARTIDO   
    ------------------------------------
    """)

        # Mostrar los partidos disponibles para registrar resultados
        num = 1
        for partido in partidos:
            print(f"{num}. {partido['fecha']} - {partido['equipo_local']} vs {partido['equipo_visitante']}")
            num += 1

        # Validar el número del partido elegido sin usar len()
        partido_elegido = int(input("Ingresa el numero del partido: ")) - 1
        while partido_elegido < 0 or partido_elegido >= num - 1:  # 'index - 1' da el tamaño de la lista
            print("Tu marcacion fue incorrecta. Intenta de nuevo")
            partido_elegido = int(input("Ingresa el numero del partido: ")) - 1

        # Preguntar al usuario quién ganó
        print("---SELECCIONA AL EQUIPO GANADOR---")
        print(f"1. {partidos[partido_elegido]['equipo_local']}")
        print(f"2. {partidos[partido_elegido]['equipo_visitante']}")
        print("3. Empate")
        equipo_win = int(input("-> "))
        goles_win = int(input("Cuantos goles hizo? -> "))

        # Inicializar puntos
        puntos_equipo_1 = 0
        puntos_equipo_2 = 0
        
        # Asignar puntos según el resultado
        if equipo_win == 1:
            puntos_equipo_1 = 3
        elif equipo_win == 2:
            puntos_equipo_2 = 3
        else:
            puntos_equipo_1 = 1
            puntos_equipo_2 = 1

        # Mostrar el estado de los equipos antes de la actualización
        print("Estado de los equipos antes de registrar el resultado:")
        for equipo in equipos:
            print(f"Equipo: {equipo['nombre']}, Puntos: {equipo['puntos']}")

        # Actualizar los puntos de los equipos
        for equipo in equipos:
            if equipo['nombre'] == partidos[partido_elegido]['equipo_local']:  # Equipo 1
                equipo['puntos'] += puntos_equipo_1  # Actualizar puntos
            elif equipo['nombre'] == partidos[partido_elegido]['equipo_visitante']:  # Equipo 2
                equipo['puntos'] += puntos_equipo_2  # Actualizar puntos

        # Mostrar el estado de los equipos después de la actualización
        print("Estado de los equipos después de registrar el resultado:")
        for equipo in equipos:
            print(f"Equipo: {equipo['nombre']}, Puntos: {equipo['puntos']}")

        print("Resultado registrado con éxito!")

        # Preguntar si desea registrar otro resultado o volver al menú principal
        continuar = input("¿Te gustaría ingresar otro resultado? SI(1) NO(2): ")
        if continuar.upper() != '1':
            print("Volviendo al menú principal...")
            break  # Salir del ciclo y volver al menú principal
        input("Presiona ENTER para continuar ->")