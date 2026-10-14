def ordenamiento_burbuja(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ordenamiento_seleccion(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def ordenamiento_insercion(lista):
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr

def quicksort(lista):
    if len(lista) <= 1:
        return lista.copy()
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    return quicksort(izq) + centro + quicksort(der)

def pedir_lista():
    entrada = input("Ingresa los números separados por comas (ej. 9, 3, 7, 1, 4): ")
    lista = [int(x.strip()) for x in entrada.split(",")]
    return lista

def menu():
    print("SISTEMA DE MÉTODOS DE ORDENAMIENTO EN PYTHON")
    lista_original = pedir_lista()
    print(f"Lista original ingresada: {lista_original}\n")

    while True:
        print("1. Ordenar con algoritmo de Burbuja (Bubble Sort)")
        print("2. Ordenar con algoritmo de Selección (Selection Sort)")
        print("3. Ordenar con algoritmo de Inserción (Insertion Sort)")
        print("4. Ordenar con algoritmo QuickSort")
        print("5. Ingresar una nueva lista de números")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción (1-6): ")

        if opcion == "1":
            print(f"Resultado (Bubble Sort): {ordenamiento_burbuja(lista_original)}\n")
        elif opcion == "2":
            print(f"Resultado (Selection Sort): {ordenamiento_seleccion(lista_original)}\n")
        elif opcion == "3":
            print(f"Resultado (Insertion Sort): {ordenamiento_insercion(lista_original)}\n")
        elif opcion == "4":
            print(f"Resultado (QuickSort): {quicksort(lista_original)}\n")
        elif opcion == "5":
            lista_original = pedir_lista()
            print(f"Lista original ingresada: {lista_original}\n")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.\n")

if __name__ == "__main__":
    menu()