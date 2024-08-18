numbers = []
while True:
    command = input().split()
    if len(command) == 1:
        break

    if command[0] == 'A':
        numbers.append(int(command[1]))
    else:
        filtered = [n for n in numbers if n % int(command[1]) == 0]
        print(sum(filtered))
