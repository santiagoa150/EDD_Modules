# Definir los movimientos válidos del caballo
movimientos_caballo = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def es_valida(x, y):
    return 1 <= x <= 8 and 1 <= y <= 8


def min_movimientos_caballo(origen, destino):
    x_origen, y_origen = origen
    x_destino, y_destino = destino

    visitado = [[False] * 9 for _ in range(9)]
    cola = [(x_origen, y_origen, 0)]

    while cola:
        x, y, movimientos = cola.pop(0)
        if x == x_destino and y == y_destino:
            return movimientos

        for dx, dy in movimientos_caballo:
            nuevo_x, nuevo_y = x + dx, y + dy
            if es_valida(nuevo_x, nuevo_y) and not visitado[nuevo_x][nuevo_y]:
                visitado[nuevo_x][nuevo_y] = True
                cola.append((nuevo_x, nuevo_y, movimientos + 1))

    return -1


# Lectura de la entrada
C = int(input())
resultados = []

for _ in range(C):
    origen, destino = input().split()
    x_origen, y_origen = ord(origen[0]) - ord('A') + 1, int(origen[1])
    x_destino, y_destino = ord(destino[0]) - ord('A') + 1, int(destino[1])

    resultado = min_movimientos_caballo((x_origen, y_origen), (x_destino, y_destino))
    resultados.append(resultado)

# Impresión de la salida
for resultado in resultados:
    print(resultado)
