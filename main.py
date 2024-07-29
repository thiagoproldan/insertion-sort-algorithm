def insertion_sort(arr):
    # Iterate from the second element to the last element / Iterar do segundo elemento até o último elemento / Iterar desde el segundo elemento hasta el último elemento
    for i in range(1, len(arr)):
        # The element to be placed at the correct position / O elemento a ser colocado na posição correta / El elemento a colocar en la posición correcta
        key = arr[i]
        # Start with the element just before the key / Comece com o elemento imediatamente anterior à chave / Comenzar con el elemento inmediatamente anterior a la clave
        j = i - 1
        # Shift elements of the sorted segment to the right until the correct position for key is found / Deslocar elementos do segmento ordenado para a direita até encontrar a posição correta para a chave / Desplazar elementos del segmento ordenado hacia la derecha hasta encontrar la posición correcta para la clave
        while j >= 0 and key < arr[j]:
            # Shift the larger element one position to the right / Deslocar o elemento maior uma posição para a direita / Desplazar el elemento mayor una posición a la derecha
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at its correct position / Inserir a chave na posição correta / Insertar la clave en su posición correcta
        arr[j + 1] = key

# Example usage / Exemplo de uso / Ejemplo de uso
if __name__ == "__main__":
    # Unsorted array / Array não ordenado / Arreglo no ordenado
    arr = [5, 3, 8, 4, 2]
    # Print the unsorted array / Imprimir o array não ordenado / Imprimir el arreglo no ordenado
    print("Unsorted array: ", arr)

    # Sort the array using Insertion Sort / Ordenar o array usando Insertion Sort / Ordenar el arreglo usando Insertion Sort
    insertion_sort(arr)
    # Print the sorted array / Imprimir o array ordenado / Imprimir el arreglo ordenado
    print("Sorted array: ", arr)

