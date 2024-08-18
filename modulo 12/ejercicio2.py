# Lectura de datos
n = int(input())
words = [input().strip() for _ in range(n)]
t = int(input())
prefixes = [input().strip() for _ in range(t)]

# Creación de un diccionario para contar palabras con cada prefijo
word_count = {}
for word in words:
    for i in range(len(word)):
        prefix = word[:i + 1]
        if prefix in word_count:
            word_count[prefix] += 1
        else:
            word_count[prefix] = 1

# Conteo de palabras con cada prefijo
for prefix in prefixes:
    count = word_count.get(prefix, 0)
    print(count)
