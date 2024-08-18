def find_longest_prefix(phones):
    if not phones:
        return '-'

    phones.sort()  # Ordenar la lista de teléfonos para comparar fácilmente
    shortest = phones[0]
    longest = phones[-1]
    prefix = ''

    for i in range(len(shortest)):
        if shortest[i] != longest[i]:
            break
        prefix += shortest[i]

    if prefix:
        return prefix
    else:
        return '-'


# Lectura de datos
while True:
    t = int(input())
    if t == 0:
        break

    phone_numbers = [input().strip() for _ in range(t)]
    result = find_longest_prefix(phone_numbers)
    print(result)