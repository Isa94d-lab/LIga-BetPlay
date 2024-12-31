def crear_equipo(equipos):
    print("""
    -------------------------------
       CREA UNO O VARIOS EQUIPOS   
    -------------------------------
    """)
    # Le pedimos al usuario que ingrese cuántos equipos le gustaría registrar
    while True:
        try: 
            numero_equipos = int(input("Cuantos equipos te gustaria ingresar? : "))
            break
        except ValueError: 
            print("TU MARCACION FUE INCORRECTA, Ingresa un numero")
            input("Presiona ENTER para regresar al menu principal ->")
    
    # Usamos el for para que i cree los equipos hasta el número que haya ingresado el usuario 
    for i in range(numero_equipos):
        # Le pedimos al usuario que ingrese el nombre del equipo
        nombre_equipo = input(f"Ingrese el nombre del equipo {i + 1}: ")
        # Añadimos el "nombre_equipo" a la lista principal de equipos como un diccionario
        equipos.append({
            'nombre': nombre_equipo,
            'jugadores': [],
            'equipo_tecnico': [],
            'puntos': 0,
            'goles': 0
        })
    print("Tus equipos han sido guardados")
    input("Presiona ENTER para continuar ->")