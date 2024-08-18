robots = set(n for n in range(1, int(input()) + 1))
while True:
    text = input()
    if text == '#':
        break

    data = tuple(text.split())
    if data[0] == 'new':
        new_num = sum([int(data[1]), int(data[2])])
        while new_num in robots:
            new_num += 1
        robots.add(new_num)
    if data[0] == 'search':
        if int(data[1]) in robots:
            print('existe')
        else:
            print('no existe')