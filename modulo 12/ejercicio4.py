def total_chars_needed(names):
    abbreviated = set()

    for name in names:
        for i in range(len(name)):
            prefix = name[:i + 1]
            if prefix not in abbreviated:
                abbreviated.add(prefix)
                break

    return sum(len(abbrev) for abbrev in abbreviated)


# Lectura de datos
while True:
    a = int(input())
    if a == 0:
        break

    asteroid_names = [input().strip() for _ in range(a)]
    result = total_chars_needed(asteroid_names)
    print(result)
