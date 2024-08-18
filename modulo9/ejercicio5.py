data = {
    'F': set(),
    'G': set()
}

while True:
    line = input()
    if line == '0':
        break
    ISBN, client = line.split()
    ISBN = int(ISBN)
    if client == 'F' and ISBN in data['G']:
        if ISBN % 2 == 0:
            data[client].add(ISBN)
            data['G'].remove(ISBN)
    elif client == 'G' and ISBN in data['F']:
        if ISBN % 2 != 0:
            data[client].add(ISBN)
            data['F'].remove(ISBN)
    else:
        data[client].add(ISBN)

print(len(data['F']), len(data['G']))
