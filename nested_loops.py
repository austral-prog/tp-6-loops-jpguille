def flatten(matrix):

    new = []
    for element in matrix:
        for i in element:
            new.append(i)
    return new


def row_sums(matrix):
    new = []
    for element in matrix:
        suma = 0
        for i in element:
            suma += i
        new.append(suma)
    return new

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    new = []
    x = len(matrix[0])
    for i in range(x):
        total = 0
        for element in matrix:
            total += element[i]
        new.append(total)
    return new
