live = set()
dead = set()

while True:
    text = input()
    if text == 'E':
        break
    case, person = text.split()

    if case == 'B':
        if person not in dead:
            live.add(person)
    elif case == 'D':
        if person in live:
            live.remove(person)
            dead.add(person)
    else:
        if person in dead:
            dead.remove(person)
            live.add(person)
print(len(live))