def registro_plantel(equipos):
    while True: 
        print("""
        ----------------------------------
           INGRESAR DATOS A LOS EQUIPOS   
        ----------------------------------
        """)
        # Le mostramos al usuario cuáles equipos están disponibles
        print("Equipos disponibles:")
        # Usamos el for para que muestre uno a uno los equipos que registramos anteriormente 
        for i in range(len(equipos)):
            print(f"{i + 1}. {equipos[i]['nombre']}")
        # El usuario seleccionará el equipo al que le quiere ingresar jugadores
        equipo_seleccionado = int(input("Seleccione el equipo al que deseas ingresar jugadores (segun su numero en la tabla): ")) - 1
        
        # Le preguntamos al usuario cuántos jugadores va a registrar
        while True:
            try: 
                numero_jugadores = int(input("Cuantos jugadores deseas registrar en este equipo?: "))
                break
            except ValueError: 
                print("TU MARCACION FUE INCORRECTA, Ingresa un numero")
                input("Presiona ENTER para regresar al menu principal ->")
        
        # Con el for le pedimos al usuario que ingrese los datos de cada jugador
        for j in range(numero_jugadores):
            nombre_jugador = input(f"Ingresa el nombre del jugador {j + 1}: ")
            dorsal_jugador = int(input("Ingresa el dorsal del jugador: "))
            posicion_jugador = input("Ingresa la posición del jugador: ")
            # Añadimos los datos del jugador al equipo seleccionado
            equipos[equipo_seleccionado]['jugadores'].append({
                'nombre': nombre_jugador,
                'dorsal': dorsal_jugador,
                'posicion': posicion_jugador
            })
        
        print(f"Se han registrado {numero_jugadores} jugadores en el equipo {equipos[equipo_seleccionado]['nombre']}.")
        
        # Preguntar si desea continuar registrando jugadores en otros equipos
        continuar = input("Deseas volver a añadir datos? SI(1) NO(2): ")
        if continuar.upper() != '1':
            input("Presiona ENTER para continuar -> ")
            break  # Salir del ciclo y volver al menu principal