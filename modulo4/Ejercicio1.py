from collections import deque

first_input = input().split()
n = int(first_input[0])
t = int(first_input[1])
sellers = deque([])
for _ in range(n):
    sellers.append(tuple(map(int, input().split())))

i = 1
last = None
while len(sellers) > 0 and t > 0:
    if i % 5 != 0:
        t -= sellers[0][1]
        last = sellers.popleft()
        sellers.append(last)
    else:
        t -= sellers[0][1]
        last = sellers.popleft()

    if t <= 0:
        last = last[:1] + (t + last[1],)
    i += 1

if t > 0:
    print("quedaron boletas disponibles")
else:
    print(last[0], last[1])

