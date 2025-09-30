import random


################EJERCICIO 1

#APARTADO A
def ordenador_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res



"""
#APARTADO B, C

def usuario_decide_jugada():
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    return eleccion_usuario


#APARTADO D

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    

"""



################EJERCICIO 2

#APARTADO A

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario




def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    
    # Jugadas
    jugada_usuario = usuario_decide_jugada()
    jugada_pc = ordenador_decide_jugada()
    
    # Mostrar jugada del ordenador
    print(f"El ordenador eligió: {jugada_pc}")
    
    # Determinar resultado
    if jugada_usuario == jugada_pc:
        print("¡Empate!")
    elif (jugada_usuario == "piedra" and jugada_pc == "tijeras") or \
         (jugada_usuario == "papel" and jugada_pc == "piedra") or \
         (jugada_usuario == "tijeras" and jugada_pc == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste...")



if __name__ == "__main__":
    jugar()
