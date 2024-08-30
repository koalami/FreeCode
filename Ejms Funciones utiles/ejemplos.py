# Ejemplos de comandos básicos en Python con métodos y clases

# Método para ordenar una lista de números
def ejemplo_sort():
    numeros = [5, 2, 9, 1, 5, 6]
    print("Lista original:", numeros)
    
    # Ordenar lista de manera ascendente
    numeros.sort()
    print("Lista ordenada (ascendente):", numeros)
    
    # Ordenar lista de manera descendente
    numeros.sort(reverse=True)
    print("Lista ordenada (descendente):", numeros)

# Método para calcular la longitud de una lista
def ejemplo_len():
    frutas = ['manzana', 'plátano', 'cereza', 'durazno']
    print("Lista de frutas:", frutas)
    
    # Calcular longitud de la lista
    longitud = len(frutas)
    print("Longitud de la lista de frutas:", longitud)

# Método para buscar un elemento en una lista
def ejemplo_busqueda():
    elementos = ['agua', 'fuego', 'tierra', 'aire']
    buscar = 'fuego'
    print("Lista de elementos:", elementos)
    
    # Buscar un elemento en la lista
    if buscar in elementos:
        print(f"Elemento '{buscar}' encontrado en la lista.")
    else:
        print(f"Elemento '{buscar}' no encontrado en la lista.")

# Método para comparar dos listas utilizando ciclos anidados
def ejemplo_comparacion_listas():
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    
    # Comparar listas usando ciclos anidados
    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                print(f"Elemento común encontrado: {item1}")

# Método para uso de condicionales y manipulación de strings
def ejemplo_strings():
    texto = "Hola Mundo"
    print("Texto original:", texto)
    
    # Convertir a minúsculas
    texto_minuscula = texto.lower()
    print("Texto en minúsculas:", texto_minuscula)
    
    # Convertir a mayúsculas
    texto_mayuscula = texto.upper()
    print("Texto en mayúsculas:", texto_mayuscula)

# Clases para ilustrar herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Método para probar las clases y herencia
def ejemplo_clases():
    perro = Perro("Firulais")
    gato = Gato("Whiskers")
    
    print(f"{perro.nombre} dice: {perro.hacer_sonido()}")
    print(f"{gato.nombre} dice: {gato.hacer_sonido()}")
    
    
    
    
def encontrar_pares_con_suma(lista, suma_objetivo):
    pares = []  # Lista para almacenar los pares que cumplen con la condición

    # Iteramos sobre cada elemento de la lista con un índice
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):  # Comparamos con los elementos siguientes
            if lista[i] + lista[j] == suma_objetivo:
                pares.append((lista[i], lista[j]))  # Añadimos el par a la lista de pares

    return pares


# Metodo de palindromos
def es_palindromo_string(cadena):
    # Convertir a minúsculas y eliminar espacios en blanco
    cadena_procesada = cadena.replace(" ", "").lower()
    
    # Verificar si la cadena es igual a su inversa
    return cadena_procesada == cadena_procesada[::-1]

def procesar_diccionario(diccionario):
    # Crear un diccionario para contar ocurrencias de cada palabra
    conteo_palabras = {}
    
    # Contar ocurrencias de cada palabra
    for palabra in diccionario:
        conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

    # Crear listas para palabras únicas y repetidas
    palabras_unicas = [palabra for palabra, conteo in conteo_palabras.items() if conteo == 1]
    palabras_repetidas = [palabra for palabra, conteo in conteo_palabras.items() if conteo > 1]

    return palabras_unicas, palabras_repetidas

# Método principal para ejecutar todas las pruebas
def pruebas():
    print("Prueba de ordenamiento de lista:")
    ejemplo_sort()
    print("\nPrueba de longitud de lista:")
    ejemplo_len()
    print("\nPrueba de búsqueda en lista:")
    ejemplo_busqueda()
    print("\nPrueba de comparación de listas:")
    ejemplo_comparacion_listas()
    print("\nPrueba de manipulación de strings:")
    ejemplo_strings()
    print("\nPrueba de clases y herencia:")
    ejemplo_clases()
    
    
    resultado = encontrar_pares_con_suma(numeros, suma_objetivo)
    print(f"Pares en la lista que suman {suma_objetivo}: {resultado}")
    print(f"¿La cadena '{cadena1}' es un palíndromo?: {es_palindromo_string(cadena1)}")  # True
    print(f"¿La cadena '{cadena2}' es un palíndromo?: {es_palindromo_string(cadena2)}")  # True
    print(f"¿La cadena '{cadena3}' es un palíndromo?: {es_palindromo_string(cadena3)}")  # False
    
    
    palabras_unicas, palabras_repetidas = procesar_diccionario(diccionario_palabras)
    print(f"Palabras únicas: {palabras_unicas}")  # ['naranja', 'melon']
    print(f"Palabras repetidas: {palabras_repetidas}")  # ['manzana', 'pera']

# Lista de ejemplo
numeros = [10, 20, 30, 40, 60, 55]


# Ejemplo de uso palindromo
cadena1 = "Anita lava la tina"
cadena2 = "A man a plan a canal Panama"
cadena3 = "Python no es palindromo"

#Ejemplo de uso
diccionario_palabras = ['manzana', 'pera', 'manzana', 'naranja', 'pera', 'melon']


# Suma objetivo
suma_objetivo = 60
# Ejecutar todas las pruebas
if __name__ == "__main__":
    pruebas()
