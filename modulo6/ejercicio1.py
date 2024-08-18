import heapq

people = []
last = -1
while True:
    line = input()
    if line == 'end':
        print(last)
        break
    elif line == 'sig':
        if len(people) > 0:
            last = heapq.heappop(people)
    else:
        heapq.heappush(people, int(line))
