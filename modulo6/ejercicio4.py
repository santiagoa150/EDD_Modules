import heapq

for _ in range(int(input())):
    length = int(input())
    line = list(map(int, input().split()))
    heapq.heapify(line)
    num1 = []
    num2 = []
    while length > 0:
        if length % 2 == 0:
            num1.append(heapq.heappop(line))
        else:
            num2.append(heapq.heappop(line))
        length -= 1
    print(int(''.join(map(str, num1))) + int(''.join(map(str, num2))))
