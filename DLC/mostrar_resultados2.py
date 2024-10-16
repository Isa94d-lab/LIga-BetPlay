
def mostrar_equipos(equipos):
    print("""
    ---------------------------
        EQUIPOS Y SUS DATOS   
    ---------------------------
    """)
    print("-------------------------------------")
    for equipo in equipos:  
        # Mostramos el nombre del equipo y los puntos
        print(f"Equipo: {equipo['nombre']} (Puntos: {equipo['puntos']})") 
        print("-------------------------------------")
        print("---JUGADORES---")
        for jugador in equipo['jugadores']: 
            print(f"    - Nombre: {jugador['nombre']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}")
        print("-------------------------------------")
        print("---EQUIPO TÉCNICO---")
        for miembro in equipo['equipo_tecnico']:
            print(f"    - {miembro}")
        input("Presiona ENTER para continuar ->")