collections = {
    'F': set(),
    'V': set(),
    'A': set(),
}

while True:
    text = input()
    if text == '#':
        break
    person, num = text.split()
    collections[person].add(int(num))
    collections['A'].add(int(num))

print(len(collections['F']), len(collections['V']), len(collections['A']))