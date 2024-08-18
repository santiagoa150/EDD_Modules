from collections import deque

for i in range(int(input())):
    tower_size = int(input())
    towers: dict[str, deque] = {
        'A': deque([n + 1 for n in range(tower_size)]),
        'B': deque([]),
        'C': deque([]),
    }
    invalid = False

    texts = []
    while True:
        text = input()
        if text == 'X X':
            break
        texts.append(text.split())

    for text in texts:
        if len(towers[text[0]]) == 0:
            invalid = True
            break

        if text[0] != text[1]:
            if len(towers[text[1]]) == 0 or towers[text[0]][0] < towers[text[1]][0]:
                towers[text[1]].appendleft(towers[text[0]].popleft())
            else:
                invalid = True
                break

    if invalid:
        print('secuencia invalida')
    elif towers['C'] == deque([n + 1 for n in range(tower_size)]):
        print('soluciona la torre')
    else:
        print('no soluciona la torre')