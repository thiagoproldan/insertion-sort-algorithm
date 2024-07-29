<details open>
    <summary>en-US</summary>

## Introduction
The Insertion Sort Algorithm is a simple sorting algorithm that builds the final sorted array one element at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it has the advantage of being simple to implement and efficient for small data sets or nearly sorted data.

## Algorithm Steps
1. Iterate from the second element to the last element.
2. For each element, compare it with the elements before it.
3. Shift the elements one position to the right until the correct position for the element is found.
4. Insert the element at its correct position.
5. Repeat until the entire array is sorted.

## Example:
Let's sort the array `[5, 3, 8, 4, 2]` using Insertion Sort.
1. Start with the second element (3). Compare it with the first element (5). Since 3 < 5, move 5 one position to the right and insert 3 at the beginning. Array becomes `[3, 5, 8, 4, 2]`.
2. Move to the next element (8). Since 8 > 5, it stays in place. Array remains `[3, 5, 8, 4, 2]`.
3. Next, compare 4 with 8 and 5. Move both elements one position to the right and insert 4 before 5. Array becomes `[3, 4, 5, 8, 2]`.
4. Finally, insert 2 in the correct position, shifting all elements as needed. Final array: `[2, 3, 4, 5, 8]`.

## Conclusion
Insertion Sort is not the most efficient algorithm for large datasets due to its O(n^2) time complexity. However, it is simple, efficient for small or nearly sorted data, and stable (preserves the relative order of equal elements).

## Example in Python
``` Python
def insertion_sort(arr):
  # Iterate from the second element to the last element
  for i in range(1, len(arr)):
    key = arr[i] # The element to be placed at the correct position
    j = i - 1 # Start with the element just before the key
    # Shift elements of the sorted segment to the right until the correct position for key is found
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j] # Shift the larger element one position to the right
      j -= 1
    arr[j + 1] = key # Insert the key at its correct position

# Example usage
if __name__ == "__main__":
  arr = [5, 3, 8, 4, 2] # Unsorted array
  print("Unsorted array: ", arr) # Print the unsorted array

  insertion_sort(arr) # Sort the array using Insertion Sort
  print("Sorted array: ", arr) # Print the sorted array
```

## Explanation
1. **Function Definition**: The `insertion_sort` function takes a list `arr` as its parameter.
2. **Outer Loop**: 
	- `for i in range(1, len(arr))`: This loop iterates from the second element to the end of the list.
3. **Key Selection**: The current element `key` is selected for comparison and insertion.
4. **Inner Loop**: 
	- `while j >= 0 and key < arr[j]`: This loop shifts elements of the sorted segment to the right until the correct position for `key` is found.
5. **Insertion**: The `key` is placed at the correct position within the sorted segment.
6. **Example Usage**: The example demonstrates how the algorithm works by showing the array before and after sorting.

</details>

---

<details>
    <summary>pt-BR</summary>

## Introdução
O algoritmo de ordenação Insertion Sort é um algoritmo simples que constrói o array ordenado final um elemento de cada vez. Ele é menos eficiente em listas grandes do que algoritmos mais avançados como quicksort, heapsort ou mergesort. No entanto, tem a vantagem de ser simples de implementar e eficiente para conjuntos de dados pequenos ou quase ordenados.

## Passos do Algoritmo
1. Iterar do segundo elemento até o último elemento.
2. Para cada elemento, compará-lo com os elementos anteriores.
3. Deslocar os elementos uma posição para a direita até encontrar a posição correta para o elemento.
4. Inserir o elemento na sua posição correta.
5. Repetir até que todo o array esteja ordenado.

## Exemplo
Vamos ordenar o array `[5, 3, 8, 4, 2]` usando Insertion Sort.
1. Comece com o segundo elemento (3). Compare-o com o primeiro elemento (5). Como 3 < 5, mova 5 uma posição para a direita e insira 3 no início. O array torna-se `[3, 5, 8, 4, 2]`.
2. Mova para o próximo elemento (8). Como 8 > 5, ele permanece no lugar. O array permanece `[3, 5, 8, 4, 2]`.
3. Em seguida, compare 4 com 8 e 5. Mova ambos os elementos em uma posição para a direita e insira 4 antes de 5. O array torna-se `[3, 4, 5, 8, 2]`.
4. Finalmente, insira 2 na posição correta, deslocando todos os elementos conforme necessário. Array final: `[2, 3, 4, 5, 8]`.

## Conclusão
Insertion Sort não é o algoritmo mais eficiente para grandes conjuntos de dados devido à sua complexidade de tempo O(n^2). No entanto, é simples, eficiente para dados pequenos ou quase ordenados, e estável (preserva a ordem relativa dos elementos iguais).

## Exemplo em Python
``` Python
def insertion_sort(arr):
  # Iterar do segundo elemento até o último elemento
  for i in range(1, len(arr)):
    key = arr[i]  # O elemento a ser colocado na posição correta
    j = i - 1  # Comece com o elemento imediatamente anterior à chave
    # Deslocar elementos do segmento ordenado para a direita até encontrar a posição correta para a chave
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]  # Deslocar o elemento maior uma posição para a direita
      j -= 1
    arr[j + 1] = key  # Inserir a chave na posição correta

# Exemplo de uso
if __name__ == "__main__":
  arr = [5, 3, 8, 4, 2]  # Array não ordenado
  print("Array não ordenado: ", arr)  # Imprimir o array não ordenado

  insertion_sort(arr)  # Ordenar o array usando Insertion Sort
  print("Array ordenado: ", arr)  # Imprimir o array ordenado
```

## Explicação
1. **Definição da Função**: A função `insertion_sort` recebe uma lista `arr` como parâmetro.
2. **Loop Externo**:
	- `for i in range(1, len(arr))`: Este loop itera do segundo elemento até o final da lista.
3. **Seleção de Chave**: O elemento atual `key` é selecionado para comparação e inserção.
4. **Loop Interno**:
	- `while j >= 0 and key < arr[j]`: Este loop desloca os elementos do segmento ordenado para a direita até encontrar a posição correta para `key`.
5. **Inserção**: O `key` é colocado na posição correta dentro do segmento ordenado.
6. **Exemplo de Uso**: O exemplo demonstra como o algoritmo funciona, mostrando o array antes e depois da ordenação.

</details>

---

<details>
    <summary>es-ES</summary>

## Introducción
El algoritmo de ordenación Insertion Sort es un algoritmo simple que construye la matriz ordenada final un elemento a la vez. Es mucho menos eficiente en listas grandes que algoritmos más avanzados como quicksort, heapsort o mergesort. Sin embargo, tiene la de ser simple de implementar y eficiente para conjuntos de datos pequeños o casi ordenados.

## Pasos del Algoritmo
1. Iterar desde el segundo elemento has el último elemento.
2. Para cada elemento, compararlo con los elementos anteriores.
3. Desplazar los elementos una posición a la derecha hasta encontrar la posición correcta para el elemento.
4. Insertar el elemento en su posición correcta.
5. Repetir hasta que toda la matriz esté ordenada.

## Ejemplo
Vamos a ordenar el arreglo `[5, 3, 8, 4, 2]` usando Insertion Sort.
1. Comience con el segundo elemento (3). Compararlo con el primer elemento (5). Como 3 < 5, mover 5 una posición a la derecha e insertar 3 al principio. El arreglo se convierte en `[3, 5, 8, 4, 2]`.
2. Pasa al siguiente elemento (8). Como 8 > 5, permanece en su lugar. El arreglo permanece `[3, 5, 8, 4, 2]`.
3. Luego, compare 4 con 8 y 5. Mueva ambos elementos una posición a la derecha e inserte 4 antes de 5. El arreglo se convierte en `[3, 4, 5, 8, 2]`.
4. Finalmente, inserte en la posición correcta, moviendo todos los elementos según sea necesario. Arreglo final: `[2, 3, 4, 5, 8]`.

## Conclusión
Insertion Sort no es el algoritmo más eficiente para grandes conjuntos de datos debido a su complejidad de tiempo O(n^2). Sin embargo, es eficiente para datos pequeños o casi ordenados, y estable (preserva el ordem relativo de elementos iguales).

## Ejemplo en Python
``` Python
def insertion_sort(arr):
  # Iterar desde el segundo elemento hasta el último elemento
  for i in range(1, len(arr)):
    key = arr[i]  # El elemento a colocar en la posición correcta
    j = i - 1  # Comenzar con el elemento inmediatamente anterior a la clave
    # Desplazar elementos del segmento ordenado hacia la derecha hasta encontrar la posición correcta para la clave
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]  # Desplazar el elemento mayor una posición a la derecha
      j -= 1
    arr[j + 1] = key  # Insertar la clave en su posición correcta

# Ejemplo de uso
if __name__ == "__main__":
  arr = [5, 3, 8, 4, 2]  # Arreglo no ordenado
  print("Arreglo no ordenado: ", arr)  # Imprimir el arreglo no ordenado

  insertion_sort(arr)  # Ordenar el arreglo usando Insertion Sort
  print("Arreglo ordenado: ", arr)  # Imprimir el arreglo ordenado
```

## Explicación
1. **Definición de la Función**: La función `insertion_sort` toma una lista `arr` como parámetro.
2. **Bucle Externo**:
	- `for i in range(1, len(arr))`: Este bucle itera desde el segundo elemento hasta el final de la lista.
3. **Selección de Clave**: El elemento actual `key` se selecciona para comparación e inserción.
4. **Bucle Interno**:
	- `while j >= 0 and key < arr[j]`: Este bucle desplaza los elementos del segmento ordenado a la derecha hasta encontrar la posición correcta para `key`.
5. **Inserción**: El `key` se coloca en la posición correcta dentro del segmento ordenado.
6. Ejemplo de Uso: El ejemplo muestra cómo funciona el algoritmo, mostrando la matriz antes y después de ordenar.

</details>

