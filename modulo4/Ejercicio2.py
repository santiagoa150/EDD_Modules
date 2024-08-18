from collections import deque

for _ in range(int(input())):
    stack = deque(map(int, input().split()))
    length = len(stack)
    modified = False

    if length == 1:
        print(length, stack[length - 1])

    while True:

        last = stack.pop()
        second_last = stack.pop()

        if (last + second_last) % 2 == 0:
            new_number = (last + second_last) // 2
            stack.append(new_number)
            modified = True
            length -= 1
        else:
            stack.append(second_last)
            stack.append(last)
            modified = False

        if length < 2 or not modified:
            print(length, stack[length - 1])
            break
