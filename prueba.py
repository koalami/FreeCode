import re

def validar_string(s):
    patron = r'^(a[ab]*a|b[ab]*b)$'
    return bool(re.match(patron, s))

# Lista de ejemplo
strings = ['aba', 'bab', 'aabbaa', 'bbabb', 'abba', 'baab', 'a', 'b', 'aa', 'bb', 'aaa', 'bbb', 'abab', 'baba']

# Validar cada string en la lista
for s in strings:
    if validar_string(s):
        print(f"'{s}' es válida")
    else:
        print(f"'{s}' no es válida")