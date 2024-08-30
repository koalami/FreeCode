def ejemplo_listas():
    # Crear una lista de ejemplo
    frutas = ['manzana', 'pera', 'cereza', 'durazno']
    
    # Añadir un elemento al final de la lista
    frutas.append('mango')
    print("Lista después de append:", frutas)
    
    # Insertar un elemento en una posición específica
    frutas.insert(1, 'kiwi')
    print("Lista después de insert:", frutas)
    
    # Eliminar un elemento por valor
    frutas.remove('pera')
    print("Lista después de remove:", frutas)
    
    # Eliminar el último elemento y devolverlo
    ultimo = frutas.pop()
    print("Lista después de pop:", frutas)
    print("Elemento eliminado con pop:", ultimo)
    
    # Reversar la lista
    frutas.reverse()
    print("Lista después de reverse:", frutas)
    
    # Ordenar la lista en orden ascendente
    frutas.sort()
    print("Lista después de sort:", frutas)

# Ejecución del ejemplo
ejemplo_listas()
