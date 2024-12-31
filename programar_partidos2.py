def programar_partidos(equipos, partidos):
    print("""
    ------------------------
        PROGRAMAR PARTIDOS   
    ------------------------
    """)
    print("Equipos disponibles: ")
    
    # Mostrar equipos
    for i in range(len(equipos)):
        print(f"{i + 1}. {equipos[i]['nombre']}")  # Solo el nombre del equipo
    print("¿Alguno de los equipos es visitante? SI(1) NO(2)")
    hay = int(input("Respuesta -> "))
    fecha = input("Ingrese la fecha del partido (DD/MM/YYYY): ")
    match hay:
        case 1: 
            equipo_visitante = int(input("Ingresa el número del equipo visitante: ")) - 1
            equipo_local = int(input("Ingresa el número del equipo local: ")) - 1
            partido = {
                'fecha': fecha,
                'equipo_local': equipos[equipo_local]['nombre'],  
                'equipo_visitante': equipos[equipo_visitante]['nombre'],  
                'equipo_ganador': 0,  # equipo_ganador
                'puntos_ganados': 0    # puntos_ganados
            }
        case _:
            equipo_local1 = int(input("Ingresa el número del primer equipo local: ")) - 1
            equipo_local2 = int(input("Ingresa el número del segundo equipo local: ")) - 1
            partido = {
                'fecha': fecha,
                'equipo_local': equipos[equipo_local1]['nombre'],  
                'equipo_visitante': equipos[equipo_local2]['nombre'],  
                'equipo_ganador': 0,  # equipo_ganador
                'puntos_ganados': 0    # puntos_ganados
            }

    partidos.append(partido)
    input("Presiona ENTER para continuar ->")