def ejemplo_comprehensions():
    # List comprehension para crear una lista de cuadrados
    cuadrados = [x**2 for x in range(10)] # rango 0-9
    print("Lista de cuadrados:", cuadrados)
    
    # Dictionary comprehension para crear un diccionario de cuadrados
    cuadrados_dict = {x: x**2 for x in range(10)}
    print("Diccionario de cuadrados:", cuadrados_dict)
    
    # List comprehension con condición que incluye pares cuadrados en orden por sort.
    pares = list(set([x for x in range(10) if x % 2 == 0] + [x**2 for x in range(10) if x % 2 == 0]))
    pares.sort()
    print("Lista de números pares:", pares)

# Ejecución del ejemplo
ejemplo_comprehensions()
