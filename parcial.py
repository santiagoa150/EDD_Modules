words = set()
shortest = ""
initial = ""
valid = True

for _ in range(int(input())):
    new_word = input()
    words.add(new_word)
    if valid:
        if initial == "":
            initial = new_word[0]
        elif new_word[0] != initial:
            valid = False
        else:
            if shortest == "" or len(new_word) < len(shortest):
                shortest = new_word

if not valid:
    print()
else:
    while True:
        initial = len(shortest)
        for n in words:
            if n[:len(shortest)] != shortest:
                shortest = shortest[:len(shortest)]

        if initial == len(shortest):
            print(shortest)
            break
