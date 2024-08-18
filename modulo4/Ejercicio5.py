from collections import deque

for _ in range(int(input())):
    info = tuple(map(int, input().split()))
    people = deque(map(int, input().split()))
    length = info[0]
    minutes = 0
    last_eliminated = 0
    current_position = info[1]
    while length > 0:
        minutes += 5
        head = people.popleft()
        current_position -= 1
        if head - 1 > 0:
            people.append(head - 1)
            if current_position == 0:
                current_position = length
        else:
            if current_position == 0:
                break
            length -= 1

    print(minutes)
