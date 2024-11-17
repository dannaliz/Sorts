class Node:
    """Clase para nodos de lista doblemente ligada."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    """Clase para lista doblemente ligada."""
    def __init__(self):
        self.head = None
        self.tail = None

    """Inicializa una lista vacía."""
    def create(self):
        self.head = None
        self.tail = None

    """Inserta un nodo en una lista vacía."""
    def insert(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node

    """Inserta un nodo a la derecha (después) de un nodo dado."""
    def insert_right(self, current, data):
        new_node = Node(data)
        if current == self.tail:  # Si es el último nodo
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        else:  # Insertar en el medio
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    """Inserta un nodo a la izquierda (antes) de un nodo dado."""
    def insert_left(self, current, data):
        new_node = Node(data)
        if current == self.head:  # Si es el primer nodo
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:  # Insertar en el medio
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
    
    """Convierte la lista enlazada a un arreglo."""
    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

"""Ordena un arreglo usando Local Insertion Sort y muestra los pasos."""
def local_insertion_sort(arr):
    linked_list = LinkedList()
    linked_list.create()  # Crear una lista vacía
    linked_list.insert(arr[0])  # Insertar el primer elemento en la lista

    print("Paso inicial:", linked_list.to_array())  # Imprimir el estado inicial

    for i in range(1, len(arr)):
        current = linked_list.head  # Siempre comenzamos desde el inicio de la lista
        inserted = False

        # Buscar dónde insertar
        while current:
            if arr[i] < current.data:
                linked_list.insert_left(current, arr[i])  # Insertar antes
                inserted = True
                break
            current = current.next

        # Si no se insertó, significa que es el mayor y va al final
        if not inserted:
            linked_list.insert_right(linked_list.tail, arr[i])

        # Imprimir el estado después de insertar el elemento actual
        print(f"Después de insertar {arr[i]}:", linked_list.to_array())

    return linked_list.to_array()



"""Ordena un arreglo usando Merge Sort."""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Dividir y ordenar recursivamente
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Mezclar y ordenar las mitades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(arr)  # arreglo con cada iteración

    return arr

""" Radix LSD para cadenas hexadecimales."""
def radix_lsd_hex(strings, k):
    for pos in range(k - 1, -1, -1):  # Del dígito menos significativo al más significativo
        buckets = [[] for _ in range(16)]

        for string in strings:  # Poner en buckets
            char = string[pos]
            value = int(char, 16)
            buckets[value].append(string)

        strings = []  
        for bucket in buckets:  # Poner lo de los buckets ya en el arreglo
            for item in bucket:
                strings.append(item)

        print(strings)  # Imprimir cada paso de la iteración

    return strings


class TreeNode:

    """Clase para nodos de árbol binario."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    """Clase para árbol binario de búsqueda."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.data:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def in_order_traversal(self, result):
        self._in_order_recursive(self.root, result)

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.data)
            self._in_order_recursive(node.right, result)

"""Ordena un arreglo usando Tree Sort. (Igual me base en el pseudocodigo de las notas de Lucy)"""
def tree_sort(arr):

    bst = BinarySearchTree()

    for value in arr:
        bst.insert(value)
        # Mostrar el árbol en orden a medida que se insertan los elementos
        sorted_result = []
        bst.in_order_traversal(sorted_result)
        print(f"Se inserta {value}: {sorted_result}")

    # Recorrer el árbol en orden para obtener el arreglo ordenado
    sorted_result = []
    bst.in_order_traversal(sorted_result)
    return sorted_result


# Programa principal
if __name__ == "__main__":
    opcion = 0
    while True:
        print("\nElige el número del método que quieres usar:\n"
                       "1. Local Insertion Sort\n"
                       "2. Merge Sort\n"
                       "3. Radix LSD\n"
                       "4. Tree Sort\n"
                       "5. Salir\n")
        opcion = int(input())
        if opcion == 1:
            array = [5, 3, 7, 2, 8, 1, 4]
            print("Original:", array)
            sorted_array = local_insertion_sort(array)
            print("Ordenado:", sorted_array)

        elif opcion == 2: 
            secuencia = [38, 27, 43, 3, 9, 82, 10]
            print("Original:", secuencia)
            secuencia_ordenada = merge_sort(secuencia)
            print("Ordenada:", secuencia_ordenada)

        elif opcion == 3:
            cadenas = ["1A3F", "4B2C", "FF00", "0A1B", "BEEF", "1234"]
            k = 4
            print("Cadena original:", cadenas)
            cadenas_ordenadas = radix_lsd_hex(cadenas, k)
            print("Cadena ordenada:", cadenas_ordenadas)

        elif opcion == 4: 
            array = [5, 3, 7, 2, 8, 1, 4]
            print("Original:", array)
            sorted_array = tree_sort(array)
            print("Ordenado:", sorted_array)

        elif opcion == 5:
            print("Adiosss")
            break
        else: 
            print("No tenemos esa opción")
