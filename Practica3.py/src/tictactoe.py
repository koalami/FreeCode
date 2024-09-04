def crear_tablero():
    return [["" for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
        


def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all (celda== jugador for celda in fila):
            return True
        
    for columna in range(3):
        if all (tablero[columna] == jugador for fila in tablero):
            return True
        
    if all (tablero[i][i] == jugador for i in range(3)) or all (tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(celda!= "" for fila in tablero for celda in fila) 


def jugar():
    tablero = crear_tablero()
    imprimir_tablero(tablero)
    
    jugador_actual = "X"
    while True:
        imprimir_tablero(tablero)
        print(f"Turno jugador {jugador_actual}")
        fila, columna = map(int, input("Ingrese fila y columna separadas por un espacio: ").split())
        
        if (tablero[fila-1][columna-1] != "") or (fila == 0) or (columna==0):
            print("Celda ocupada. Elija otra celda.")
            continue
        
        tablero[fila-1][columna-1] = jugador_actual
      
        
        if verificar_ganador(tablero, jugador_actual):
            print(f"El jugador {jugador_actual} gana!")
            imprimir_tablero(tablero)
            print(f"Gano, {jugador_actual} ")
            break
        
        if tablero_lleno(tablero):
            print("Tablero lleno. Empate!")
            print("Empate")
            break
        
        jugador_actual = "O" if jugador_actual == "X" else "X"
        
if __name__ == "__main__":
    jugar()