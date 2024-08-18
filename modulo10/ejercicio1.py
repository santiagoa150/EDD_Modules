words = {}
for _ in range(int(input())):
    ewokes, spanish = input().split()
    words[ewokes] = spanish

while True:
    to_translate = input()
    if to_translate == '#':
        break
    try:
        print(words[to_translate])
    except:
        print('Entrada no encontrada')
