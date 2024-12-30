# Algoritmo de Backtracking para Resolver un Sudoku
# Paso 1: Representamos el tablero como una matriz 9x9

def imprimir_tablero(tablero):
    """Funcion para imprimir el tablero de Sudoku con subcuadrículas 3x3 separadas."""
    for i, fila in enumerate(tablero):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Línea horizontal para dividir las subcuadrículas
        for j, num in enumerate(fila):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  # Línea vertical para dividir las subcuadrículas
            print(str(num) if num != 0 else '.', end=" ")
        print()

# Verificamos si un número es válido en una celda
def es_valido(tablero, fila, columna, numero):
    """Verifica si un numero puede colocarse en una posicion dada."""
    # Verificar la fila
    for i in range(9):
        if tablero[fila][i] == numero:
            return False

    # Verificar la columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False

    # Verificar la subcuadrícula 3x3
    inicio_fila = (fila // 3) * 3
    inicio_columna = (columna // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == numero:
                return False

    return True

# Algoritmo de Backtracking para resolver el Sudoku
def resolver_sudoku(tablero):
    """Resuelve el tablero de Sudoku usando Backtracking."""
    for fila in range(9):
        for columna in range(9):
            # Buscar una celda vacía (representada por 0)
            if tablero[fila][columna] == 0:
                # Intentar rellenar la celda con un número del 1 al 9
                for numero in range(1, 10):
                    if es_valido(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero

                        # Llamada recursiva
                        if resolver_sudoku(tablero):
                            return True

                        # Retroceder si no lleva a una solución
                        tablero[fila][columna] = 0

                return False  # No se pudo rellenar esta celda

    return True  # El tablero está resuelto

if __name__ == "__main__":
    # Tablero incompleto de Sudoku (0 representa celdas vacías)
    tablero_incompleto = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Tablero inicial:")
    imprimir_tablero(tablero_incompleto)

    if resolver_sudoku(tablero_incompleto):
        print("\nTablero resuelto:")
        imprimir_tablero(tablero_incompleto)
    else:
        print("\nNo se encontró solución para el tablero dado.")
