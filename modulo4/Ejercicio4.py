from collections import deque

for _ in range(int(input())):
    code = tuple(input().split())
    code = code[:-1]
    characters = deque([])
    valid = True
    for i in code:
        if i in ['{', '[', '(']:
            characters.append(i)
        else:
            try:
                last = characters.pop()
                if (i == '}' and last != '{') or (i == ']' and last != '[') or (i == ')' and last != '('):
                    valid = False
                    break
            except:
                valid = False
                break
    if valid:
        print('correcta')
    else:
        print('incorrecta')

