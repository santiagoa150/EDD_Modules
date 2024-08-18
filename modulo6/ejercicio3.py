import heapq

for _ in range(int(input())):
    case = list(map(int, input().split()))
    case = case[:-1]
    heapq.heapify(case)
    while len(case) > 2:
        heapq.heappush(case, heapq.heappop(case) + heapq.heappop(case))

    print(' '.join(map(str, case)))
